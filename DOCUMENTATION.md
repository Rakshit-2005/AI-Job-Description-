# 🎯 AI-Enabled Intelligent Assessment & Hiring Platform

## Complete Documentation for IIT Gandhinagar Hackathon

---

## 📋 Table of Contents
1. [Project Overview](#project-overview)
2. [Features Implemented](#features-implemented)
3. [Technology Stack](#technology-stack)
4. [Architecture](#architecture)
5. [Setup Instructions](#setup-instructions)
6. [How It Works](#how-it-works)
7. [API Documentation](#api-documentation)
8. [AI Integration](#ai-integration)
9. [Security Features](#security-features)
10. [Demo Scenarios](#demo-scenarios)

---

## 🎯 Project Overview

An AI-powered assessment platform that eliminates fake job applications by evaluating candidates strictly based on job requirements. The platform uses Google Gemini AI to automatically parse job descriptions and generate role-specific assessments.

### Problem Statement Addressed
- ✅ Automatic interpretation of job descriptions
- ✅ Adaptive, role-aligned assessment generation
- ✅ Filter fake/unqualified applications
- ✅ Comprehensive evaluation with AI insights
- ✅ Anti-fraud mechanisms
- ✅ Detailed candidate analytics and leaderboards

---

## ✨ Features Implemented

### 1. Job Description Intelligence ✅
- **AI-Powered Parsing**: Extracts skills, experience level, role type, and domain knowledge using Gemini
- **Automatic Mapping**: Maps requirements to assessment criteria
- **Difficulty Calibration**: Adjusts question complexity based on experience level

### 2. Automated Question Generation ✅
- **Multiple Formats**: MCQ, Subjective, and Coding questions
- **Balanced Distribution**: Appropriate mix based on role requirements
- **Role-Specific**: Questions aligned with extracted skills
- **Adaptive Complexity**: Adjusted for fresher vs experienced roles

### 3. Smart Candidate Evaluation ✅
- **Automated Grading**: Instant evaluation for MCQ and coding questions
- **AI-Assisted Review**: Gemini evaluates subjective answers with feedback
- **Code Execution**: Real-time Python code testing with test cases
- **Weighted Scoring**: Based on skill importance

### 4. Anti-Fake Application Mechanism ✅
- **Plagiarism Detection**: TF-IDF based similarity checking
- **Anomaly Detection**: Identifies suspicious patterns:
  - Too-fast submission times
  - Random guessing patterns
  - Unrealistic score combinations
- **Resume-Performance Correlation**: Flags skill mismatches

### 5. Scoring & Leaderboards ✅
- **Comprehensive Scoring**: Overall, section-wise, skill-wise
- **Real-time Ranking**: Automatic candidate ranking
- **Live Leaderboards**: Configurable display
- **Qualification Thresholds**: Recruiter-defined cutoffs

### 6. Detailed Analytics ✅
- **Performance Reports**: Strengths, weaknesses, skill gaps
- **AI-Generated Insights**: Comprehensive evaluation summary
- **Benchmark Comparison**: Relative performance analysis
- **Exportable Reports**: Structured data for recruitment decisions

### 7. Recruiter Controls ✅
- **Job Management**: Create, edit, view jobs
- **Assessment Customization**: Duration, difficulty, weightage
- **Cut-off Configuration**: Set qualification thresholds
- **Dashboard Analytics**: Track completion rates, qualified candidates

### 8. Fairness & Transparency ✅
- **Explainable AI**: Score breakdowns and reasoning
- **Standardized Evaluation**: Consistent logic across candidates
- **Detailed Feedback**: Clear explanations for scores

---

## 🛠️ Technology Stack

### Backend
- **Framework**: FastAPI (Python 3.8+)
- **Database**: SQLite (dev) / PostgreSQL (prod ready)
- **AI Integration**: Google Gemini API
- **Authentication**: JWT with bcrypt
- **ORM**: SQLAlchemy
- **Validation**: Pydantic

### Frontend
- **Framework**: React 18
- **Build Tool**: Vite
- **Routing**: React Router v6
- **HTTP Client**: Axios
- **Styling**: Custom CSS with gradient themes

### AI & Analysis
- **LLM**: Google Gemini Pro
- **Plagiarism**: scikit-learn TF-IDF
- **Code Execution**: Python subprocess
- **Text Processing**: NLTK

### DevOps
- **Version Control**: Git
- **API Documentation**: FastAPI auto-generated Swagger/OpenAPI
- **Environment**: python-dotenv

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        Frontend (React)                      │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │Recruiter │  │Candidate │  │Assessment│  │  Results │   │
│  │Dashboard │  │Dashboard │  │Interface │  │& Leaders │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
└────────────────────────┬────────────────────────────────────┘
                         │ REST API (Axios)
┌────────────────────────┴────────────────────────────────────┐
│                    Backend (FastAPI)                         │
│  ┌─────────────────────────────────────────────────────┐   │
│  │              API Routes & Controllers                 │   │
│  └─────────────────────────────────────────────────────┘   │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │  Gemini  │  │   Code   │  │Plagiarism│  │ Anomaly  │   │
│  │  Service │  │ Executor │  │ Detector │  │ Detector │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │              Database (SQLAlchemy ORM)               │   │
│  └─────────────────────────────────────────────────────┘   │
└────────────────────────┬────────────────────────────────────┘
                         │
┌────────────────────────┴────────────────────────────────────┐
│                     External Services                        │
│  ┌──────────────┐              ┌──────────────┐            │
│  │  Gemini API  │              │   Database   │            │
│  │  (Google AI) │              │   (SQLite)   │            │
│  └──────────────┘              └──────────────┘            │
└─────────────────────────────────────────────────────────────┘
```

### Data Flow

1. **Job Creation Flow**:
   ```
   Recruiter inputs JD → Gemini parses JD → Extract skills/requirements 
   → Generate questions → Store in database → Return job ID
   ```

2. **Assessment Flow**:
   ```
   Candidate starts assessment → Fetch questions → Submit answers 
   → Evaluate (MCQ auto, Code execute, Subjective AI) 
   → Calculate scores → Detect anomalies → Generate report
   ```

3. **Evaluation Flow**:
   ```
   Complete assessment → Calculate total score → Run plagiarism check 
   → Detect anomalies → Generate AI insights → Update rankings 
   → Create comprehensive report
   ```

---

## 🚀 Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Node.js 16 or higher
- Google Gemini API key (free tier)

### Quick Start (Automated)

```powershell
# 1. Get Gemini API Key
.\get-api-key.ps1

# 2. Run setup
.\setup.ps1

# 3. Start servers
.\run.ps1
```

### Manual Setup

#### Backend
```powershell
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt

# Create .env file
copy .env.example .env
# Edit .env and add: GEMINI_API_KEY=your_key

# Run
uvicorn main:app --reload
```

#### Frontend
```powershell
cd frontend
npm install
npm run dev
```

### Access Points
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

---

## 🔄 How It Works

### For Recruiters

1. **Register/Login** with role "Recruiter"
2. **Create Job**:
   - Enter job title
   - Paste complete job description
   - Set duration and cutoff percentage
   - AI automatically parses JD and generates questions
3. **View Leaderboard**:
   - See all candidates who took the assessment
   - View detailed rankings and scores
   - Access individual candidate reports

### For Candidates

1. **Register/Login** with role "Candidate"
2. **Browse Assessments**:
   - View available job openings
   - See required skills and duration
3. **Take Assessment**:
   - Answer MCQ, subjective, and coding questions
   - Submit each answer (automatically evaluated)
   - Complete assessment
4. **View Results**:
   - See overall score and rank
   - Get section-wise performance
   - Review AI-generated feedback
   - Identify skill gaps

---

## 📡 API Documentation

### Authentication Endpoints

#### POST /register
Register new user
```json
{
  "email": "user@example.com",
  "password": "password123",
  "full_name": "John Doe",
  "role": "candidate"  // or "recruiter"
}
```

#### POST /token
Login and get JWT token
```
Form data:
username: user@example.com
password: password123
```

### Job Endpoints

#### POST /jobs (Recruiter only)
Create job with AI parsing
```json
{
  "title": "Full Stack Developer",
  "description": "Complete job description...",
  "duration_minutes": 60,
  "cutoff_percentage": 60.0
}
```

#### GET /jobs
List all active jobs

#### GET /jobs/{job_id}
Get specific job details

### Assessment Endpoints

#### POST /assessments
Start new assessment
```json
{
  "job_id": 1,
  "resume_url": "optional_resume_link"
}
```

#### GET /assessments/{assessment_id}/questions
Get questions for assessment

#### POST /assessments/{assessment_id}/submit
Submit answer
```json
{
  "question_id": 1,
  "selected_option": "A",  // for MCQ
  "answer": "text answer",  // for subjective
  "code_submission": "def solution()..."  // for coding
}
```

#### POST /assessments/{assessment_id}/complete
Complete assessment and generate report

### Results Endpoints

#### GET /assessments/{assessment_id}/results
Get detailed evaluation report

#### GET /jobs/{job_id}/leaderboard
Get leaderboard for job

---

## 🤖 AI Integration

### Gemini API Usage

1. **Job Description Parsing**
   ```python
   prompt = "Analyze this JD and extract skills, experience level, role type..."
   response = gemini.generate_content(prompt)
   parsed_data = json.loads(response.text)
   ```

2. **Question Generation**
   ```python
   prompt = f"Generate {num} questions for role with skills: {skills}..."
   response = gemini.generate_content(prompt)
   questions = json.loads(response.text)
   ```

3. **Subjective Evaluation**
   ```python
   prompt = f"Evaluate this answer: {answer} for question: {question}..."
   response = gemini.generate_content(prompt)
   evaluation = json.loads(response.text)
   ```

4. **Report Generation**
   ```python
   prompt = f"Generate evaluation report for assessment data: {data}..."
   response = gemini.generate_content(prompt)
   report = json.loads(response.text)
   ```

### Cost Analysis
- Free tier: 60 requests/minute, 1500/day
- Average assessment: ~15-20 requests (parsing + generation + evaluation)
- Sufficient for 70-100 complete assessments per day

---

## 🔒 Security Features

1. **Authentication**: JWT-based with secure password hashing (bcrypt)
2. **Authorization**: Role-based access control
3. **Input Validation**: Pydantic models for all inputs
4. **SQL Injection Prevention**: SQLAlchemy ORM parameterized queries
5. **CORS Protection**: Configured for specific origins
6. **Code Execution Safety**: Subprocess with timeout limits

---

## 🎬 Demo Scenarios

### Scenario 1: Complete Recruitment Flow
1. Recruiter creates "Full Stack Developer" job
2. 5 candidates take assessment
3. View leaderboard with rankings
4. Check top candidate's detailed report

### Scenario 2: AI Question Generation
1. Paste different JDs (Data Analyst, DevOps, etc.)
2. Show how questions adapt to role
3. Demonstrate difficulty variation

### Scenario 3: Anti-Fraud Detection
1. Simulate fast submissions
2. Show plagiarism detection
3. Display anomaly flags

### Scenario 4: Comprehensive Evaluation
1. Complete full assessment
2. Show AI-generated feedback
3. Display skill-wise breakdown
4. Highlight strengths and gaps

---

## 📊 Database Schema

```
Users (candidates & recruiters)
├── Jobs (created by recruiters)
│   └── Questions (AI-generated)
├── Assessments (candidate attempts)
│   ├── Submissions (answers to questions)
│   └── Evaluation (comprehensive report)
```

---

## 🎯 Key Differentiators

1. **Fully Automated**: From JD to questions to evaluation
2. **AI-Powered**: Gemini for intelligent parsing and evaluation
3. **Multi-Format**: MCQ + Subjective + Coding in one platform
4. **Real Code Execution**: Actually runs and tests code
5. **Anti-Fraud**: Multiple detection mechanisms
6. **Comprehensive**: End-to-end recruitment solution

---

## 📈 Future Enhancements

- Video proctoring integration
- Advanced code execution (multiple languages)
- ML-based candidate scoring
- Interview scheduling
- ATS integration
- Mobile app
- Resume parsing with AI
- Skill-based job matching

---

## 🏆 Hackathon Highlights

✅ All required features implemented
✅ Production-ready code quality
✅ Scalable architecture
✅ Beautiful, responsive UI
✅ Comprehensive documentation
✅ Easy setup and deployment
✅ Real AI integration (not mock)
✅ Working demo available

---

## 📝 License

MIT License - Feel free to use for hackathon and beyond!

---

## 👥 Support

For questions during the hackathon:
- Check API docs at /docs endpoint
- Review QUICKSTART.md for setup issues
- See SAMPLE_DATA.md for test cases

**Good luck with your presentation! 🚀**
