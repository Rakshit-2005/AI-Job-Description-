from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta
from typing import List
import uvicorn

from database import engine, get_db, Base
from models import User, Job, Question, Assessment, Submission, Evaluation
from schemas import *
from auth import verify_password, get_password_hash, create_access_token, verify_token
from gemini_service import gemini_service
from assessment_utils import code_executor, plagiarism_detector, anomaly_detector
from config import get_settings

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Assessment Platform", version="1.0.0")

settings = get_settings()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# ==================== AUTH ROUTES ====================

@app.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    """Register new user"""
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = get_password_hash(user.password)
    new_user = User(
        email=user.email,
        hashed_password=hashed_password,
        full_name=user.full_name,
        role=user.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.post("/token", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """Login and get access token"""
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )
    
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email, "role": user.role}, 
        expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """Get current authenticated user"""
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    
    email = payload.get("sub")
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# ==================== JOB ROUTES ====================

@app.post("/jobs", response_model=JobResponse)
def create_job(job: JobCreate, current_user: User = Depends(get_current_user), 
               db: Session = Depends(get_db)):
    """Create new job and parse JD with Gemini"""
    if current_user.role not in ["recruiter", "admin"]:
        raise HTTPException(status_code=403, detail="Not authorized")
    
    # Parse JD using Gemini
    jd_data = gemini_service.parse_job_description(job.description)
    
    # Create job
    new_job = Job(
        title=job.title,
        description=job.description,
        recruiter_id=current_user.id,
        required_skills=jd_data.get("required_skills", []),
        experience_level=jd_data.get("experience_level", "Mid-level"),
        role_type=jd_data.get("role_type", "General"),
        domain_knowledge=jd_data.get("domain_knowledge", []),
        duration_minutes=job.duration_minutes,
        cutoff_percentage=job.cutoff_percentage
    )
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    
    # Generate questions using Gemini
    questions = gemini_service.generate_questions(jd_data)
    
    for q_data in questions:
        question = Question(
            job_id=new_job.id,
            question_type=q_data["question_type"],
            question_text=q_data["question_text"],
            difficulty=q_data["difficulty"],
            skill_tested=q_data["skill_tested"],
            options=q_data.get("options"),
            correct_answer=q_data.get("correct_answer"),
            test_cases=q_data.get("test_cases"),
            starter_code=q_data.get("starter_code"),
            max_score=q_data["max_score"]
        )
        db.add(question)
    
    db.commit()
    
    return new_job

@app.get("/jobs", response_model=List[JobResponse])
def get_jobs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Get all active jobs"""
    jobs = db.query(Job).filter(Job.is_active == True).offset(skip).limit(limit).all()
    return jobs

@app.get("/jobs/{job_id}", response_model=JobResponse)
def get_job(job_id: int, db: Session = Depends(get_db)):
    """Get job details"""
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job

# ==================== ASSESSMENT ROUTES ====================

@app.post("/assessments", response_model=AssessmentResponse)
def create_assessment(assessment: AssessmentCreate, 
                     current_user: User = Depends(get_current_user),
                     db: Session = Depends(get_db)):
    """Start new assessment for candidate"""
    job = db.query(Job).filter(Job.id == assessment.job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    
    # Check if already taken
    existing = db.query(Assessment).filter(
        Assessment.job_id == assessment.job_id,
        Assessment.candidate_id == current_user.id
    ).first()
    
    if existing:
        raise HTTPException(status_code=400, detail="Assessment already taken")
    
    # Calculate max possible score
    questions = db.query(Question).filter(Question.job_id == assessment.job_id).all()
    max_score = sum(q.max_score for q in questions)
    
    new_assessment = Assessment(
        job_id=assessment.job_id,
        candidate_id=current_user.id,
        status="in_progress",
        started_at=datetime.utcnow(),
        max_possible_score=max_score,
        resume_url=assessment.resume_url
    )
    db.add(new_assessment)
    db.commit()
    db.refresh(new_assessment)
    
    return new_assessment

@app.get("/assessments/{assessment_id}/questions", response_model=List[QuestionResponse])
def get_assessment_questions(assessment_id: int, 
                            current_user: User = Depends(get_current_user),
                            db: Session = Depends(get_db)):
    """Get questions for assessment"""
    assessment = db.query(Assessment).filter(Assessment.id == assessment_id).first()
    if not assessment:
        raise HTTPException(status_code=404, detail="Assessment not found")
    
    if assessment.candidate_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    
    questions = db.query(Question).filter(Question.job_id == assessment.job_id).all()
    
    # Don't send correct answers for MCQ
    for q in questions:
        if q.question_type == "mcq":
            q.correct_answer = None
    
    return questions

@app.post("/assessments/{assessment_id}/submit", response_model=SubmissionResponse)
def submit_answer(assessment_id: int, submission: SubmissionCreate,
                 current_user: User = Depends(get_current_user),
                 db: Session = Depends(get_db)):
    """Submit answer for a question"""
    assessment = db.query(Assessment).filter(Assessment.id == assessment_id).first()
    if not assessment or assessment.candidate_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    
    question = db.query(Question).filter(Question.id == submission.question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    
    # Create submission
    new_submission = Submission(
        assessment_id=assessment_id,
        question_id=submission.question_id,
        answer=submission.answer,
        selected_option=submission.selected_option,
        code_submission=submission.code_submission,
        submitted_at=datetime.utcnow()
    )
    
    # Evaluate based on question type
    if question.question_type == "mcq":
        # Check MCQ answer
        is_correct = submission.selected_option == question.correct_answer
        new_submission.is_correct = is_correct
        new_submission.score = question.max_score if is_correct else 0
        new_submission.ai_feedback = "Correct!" if is_correct else f"Incorrect. Correct answer: {question.correct_answer}"
    
    elif question.question_type == "coding":
        # Execute code
        result = code_executor.execute_python_code(
            submission.code_submission,
            question.test_cases
        )
        new_submission.score = (result["score_percentage"] / 100) * question.max_score
        new_submission.is_correct = result["passed"] == result["total"]
        new_submission.ai_feedback = f"Passed {result['passed']}/{result['total']} test cases"
    
    elif question.question_type == "subjective":
        # AI evaluation
        evaluation = gemini_service.evaluate_subjective_answer(
            question.question_text,
            submission.answer,
            question.max_score
        )
        new_submission.score = evaluation["score"]
        new_submission.ai_feedback = evaluation["feedback"]
    
    # Check plagiarism
    previous_submissions = db.query(Submission).filter(
        Submission.question_id == submission.question_id,
        Submission.id != new_submission.id
    ).all()
    
    if submission.answer or submission.code_submission:
        content = submission.code_submission or submission.answer
        plagiarism_result = plagiarism_detector.check_against_database(
            content,
            [s.code_submission or s.answer for s in previous_submissions if s.code_submission or s.answer]
        )
        new_submission.plagiarism_score = plagiarism_result["max_similarity"]
        new_submission.similar_submissions = plagiarism_result["similar_submissions"]
    
    db.add(new_submission)
    db.commit()
    db.refresh(new_submission)
    
    return new_submission

@app.post("/assessments/{assessment_id}/complete")
def complete_assessment(assessment_id: int,
                       current_user: User = Depends(get_current_user),
                       db: Session = Depends(get_db)):
    """Complete assessment and generate evaluation"""
    assessment = db.query(Assessment).filter(Assessment.id == assessment_id).first()
    if not assessment or assessment.candidate_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    
    # Calculate total score
    submissions = db.query(Submission).filter(Submission.assessment_id == assessment_id).all()
    total_score = sum(s.score or 0 for s in submissions)
    
    assessment.total_score = total_score
    assessment.percentage = (total_score / assessment.max_possible_score * 100) if assessment.max_possible_score > 0 else 0
    assessment.status = "completed"
    assessment.completed_at = datetime.utcnow()
    
    # Detect anomalies
    assessment_data = {
        "submissions": [{"time_taken_seconds": 30, "selected_option": s.selected_option, 
                        "plagiarism_score": s.plagiarism_score or 0} for s in submissions],
        "total_score": total_score,
        "max_possible_score": assessment.max_possible_score
    }
    
    anomalies = anomaly_detector.detect_anomalies(assessment_data)
    if anomalies:
        assessment.is_suspicious = True
        assessment.anomaly_flags = anomalies
    
    # Calculate ranking
    job_assessments = db.query(Assessment).filter(
        Assessment.job_id == assessment.job_id,
        Assessment.status == "completed"
    ).order_by(Assessment.total_score.desc()).all()
    
    for idx, a in enumerate(job_assessments, 1):
        a.rank = idx
    
    # Generate detailed evaluation
    skill_scores = {}
    mcq_score = 0
    subjective_score = 0
    coding_score = 0
    
    for submission in submissions:
        question = db.query(Question).filter(Question.id == submission.question_id).first()
        if question:
            # Track by skill
            if question.skill_tested not in skill_scores:
                skill_scores[question.skill_tested] = []
            skill_scores[question.skill_tested].append(submission.score or 0)
            
            # Track by type
            if question.question_type == "mcq":
                mcq_score += submission.score or 0
            elif question.question_type == "subjective":
                subjective_score += submission.score or 0
            elif question.question_type == "coding":
                coding_score += submission.score or 0
    
    # Average skill scores
    skill_scores = {skill: sum(scores)/len(scores) for skill, scores in skill_scores.items()}
    
    # Generate AI report
    report_data = {
        "total_score": total_score,
        "percentage": assessment.percentage,
        "skill_scores": skill_scores,
        "is_suspicious": assessment.is_suspicious
    }
    
    ai_report = gemini_service.generate_evaluation_report(report_data)
    
    # Create evaluation
    evaluation = Evaluation(
        assessment_id=assessment_id,
        strengths=ai_report.get("strengths", []),
        weaknesses=ai_report.get("weaknesses", []),
        skill_gaps=ai_report.get("skill_gaps", []),
        skill_scores=skill_scores,
        mcq_score=mcq_score,
        subjective_score=subjective_score,
        coding_score=coding_score,
        percentile=0,  # Calculate later
        qualified=assessment.percentage >= db.query(Job).filter(Job.id == assessment.job_id).first().cutoff_percentage,
        ai_summary=ai_report.get("ai_summary", ""),
        recommendation=ai_report.get("recommendation", "")
    )
    
    db.add(evaluation)
    db.commit()
    
    return {"message": "Assessment completed", "assessment_id": assessment_id}

# ==================== RESULTS & LEADERBOARD ROUTES ====================

@app.get("/assessments/{assessment_id}/results", response_model=EvaluationResponse)
def get_results(assessment_id: int, 
                current_user: User = Depends(get_current_user),
                db: Session = Depends(get_db)):
    """Get detailed assessment results"""
    assessment = db.query(Assessment).filter(Assessment.id == assessment_id).first()
    if not assessment:
        raise HTTPException(status_code=404, detail="Assessment not found")
    
    # Allow candidate and recruiter to view
    job = db.query(Job).filter(Job.id == assessment.job_id).first()
    if assessment.candidate_id != current_user.id and job.recruiter_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    
    evaluation = db.query(Evaluation).filter(Evaluation.assessment_id == assessment_id).first()
    if not evaluation:
        raise HTTPException(status_code=404, detail="Evaluation not found")
    
    return evaluation

@app.get("/jobs/{job_id}/leaderboard", response_model=List[LeaderboardEntry])
def get_leaderboard(job_id: int, db: Session = Depends(get_db)):
    """Get leaderboard for a job"""
    assessments = db.query(Assessment, User).join(User).filter(
        Assessment.job_id == job_id,
        Assessment.status == "completed"
    ).order_by(Assessment.rank).all()
    
    leaderboard = []
    for assessment, user in assessments:
        evaluation = db.query(Evaluation).filter(
            Evaluation.assessment_id == assessment.id
        ).first()
        
        leaderboard.append(LeaderboardEntry(
            rank=assessment.rank or 0,
            candidate_name=user.full_name,
            total_score=assessment.total_score or 0,
            percentage=assessment.percentage or 0,
            skill_scores=evaluation.skill_scores if evaluation else {},
            completed_at=assessment.completed_at or assessment.created_at
        ))
    
    return leaderboard

@app.get("/")
def root():
    return {"message": "AI Assessment Platform API", "version": "1.0.0"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
