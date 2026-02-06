from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey, Boolean, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    full_name = Column(String)
    role = Column(String)  # recruiter, admin, candidate
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    jobs = relationship("Job", back_populates="recruiter")
    assessments = relationship("Assessment", back_populates="candidate")

class Job(Base):
    __tablename__ = "jobs"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    recruiter_id = Column(Integer, ForeignKey("users.id"))
    
    # Parsed JD data
    required_skills = Column(JSON)  # List of skills
    experience_level = Column(String)
    role_type = Column(String)
    domain_knowledge = Column(JSON)
    
    # Assessment config
    duration_minutes = Column(Integer, default=60)
    cutoff_percentage = Column(Float, default=60.0)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)
    
    # Relationships
    recruiter = relationship("User", back_populates="jobs")
    questions = relationship("Question", back_populates="job")
    assessments = relationship("Assessment", back_populates="job")

class Question(Base):
    __tablename__ = "questions"
    
    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer, ForeignKey("jobs.id"))
    
    question_type = Column(String)  # mcq, subjective, coding
    question_text = Column(Text)
    difficulty = Column(String)  # easy, medium, hard
    skill_tested = Column(String)
    
    # MCQ specific
    options = Column(JSON)  # List of options
    correct_answer = Column(String)
    
    # Coding specific
    test_cases = Column(JSON)
    starter_code = Column(Text)
    
    # Scoring
    max_score = Column(Float)
    weightage = Column(Float, default=1.0)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    job = relationship("Job", back_populates="questions")
    submissions = relationship("Submission", back_populates="question")

class Assessment(Base):
    __tablename__ = "assessments"
    
    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer, ForeignKey("jobs.id"))
    candidate_id = Column(Integer, ForeignKey("users.id"))
    
    # Status
    status = Column(String, default="not_started")  # not_started, in_progress, completed
    started_at = Column(DateTime)
    completed_at = Column(DateTime)
    
    # Scores
    total_score = Column(Float, default=0.0)
    max_possible_score = Column(Float)
    percentage = Column(Float)
    rank = Column(Integer)
    
    # Flags
    is_suspicious = Column(Boolean, default=False)
    anomaly_flags = Column(JSON)  # List of detected issues
    
    # Resume analysis
    resume_url = Column(String)
    resume_skills = Column(JSON)
    skill_match_score = Column(Float)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    job = relationship("Job", back_populates="assessments")
    candidate = relationship("User", back_populates="assessments")
    submissions = relationship("Submission", back_populates="assessment")
    evaluation = relationship("Evaluation", back_populates="assessment", uselist=False)

class Submission(Base):
    __tablename__ = "submissions"
    
    id = Column(Integer, primary_key=True, index=True)
    assessment_id = Column(Integer, ForeignKey("assessments.id"))
    question_id = Column(Integer, ForeignKey("questions.id"))
    
    # Answer data
    answer = Column(Text)
    selected_option = Column(String)  # For MCQ
    code_submission = Column(Text)  # For coding
    
    # Evaluation
    score = Column(Float)
    is_correct = Column(Boolean)
    ai_feedback = Column(Text)
    
    # Time tracking
    time_taken_seconds = Column(Integer)
    submitted_at = Column(DateTime, default=datetime.utcnow)
    
    # Plagiarism
    plagiarism_score = Column(Float)
    similar_submissions = Column(JSON)
    
    # Relationships
    assessment = relationship("Assessment", back_populates="submissions")
    question = relationship("Question", back_populates="submissions")

class Evaluation(Base):
    __tablename__ = "evaluations"
    
    id = Column(Integer, primary_key=True, index=True)
    assessment_id = Column(Integer, ForeignKey("assessments.id"))
    
    # Overall analysis
    strengths = Column(JSON)
    weaknesses = Column(JSON)
    skill_gaps = Column(JSON)
    
    # Skill-wise breakdown
    skill_scores = Column(JSON)  # {skill: score}
    
    # Section-wise performance
    mcq_score = Column(Float)
    subjective_score = Column(Float)
    coding_score = Column(Float)
    
    # Ranking info
    percentile = Column(Float)
    qualified = Column(Boolean)
    
    # AI insights
    ai_summary = Column(Text)
    recommendation = Column(Text)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    assessment = relationship("Assessment", back_populates="evaluation")
