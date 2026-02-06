# AI Assessment Platform - Quick Start Guide

## 🚀 Features

✅ **JD Parsing with Gemini AI** - Automatically extract skills, experience level, and requirements
✅ **Auto Question Generation** - Generate MCQ, subjective, and coding questions
✅ **AI-Powered Evaluation** - Gemini evaluates subjective answers and code
✅ **Plagiarism Detection** - Detect similar submissions using TF-IDF
✅ **Code Execution** - Run and test Python code submissions
✅ **Anomaly Detection** - Flag suspicious behavior patterns
✅ **Leaderboard & Rankings** - Real-time candidate rankings
✅ **Detailed Analytics** - Comprehensive skill-wise reports

## 📋 Prerequisites

- Python 3.8+
- Node.js 16+
- Google Gemini API Key (free tier available)

## 🛠️ Installation

### Option 1: Automated Setup (Recommended)

```powershell
# Run setup script
.\setup.ps1

# Edit .env file and add your Gemini API key
# backend\.env -> GEMINI_API_KEY=your_key_here

# Run both servers
.\run.ps1
```

### Option 2: Manual Setup

#### Backend Setup
```powershell
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt

# Copy and edit .env
copy .env.example .env
# Add your GEMINI_API_KEY in .env

# Run backend
uvicorn main:app --reload
```

#### Frontend Setup
```powershell
cd frontend
npm install
npm run dev
```

## 🔑 Get Gemini API Key

1. Go to: https://makersuite.google.com/app/apikey
2. Click "Create API Key"
3. Copy the key
4. Add to `backend\.env`: `GEMINI_API_KEY=your_key_here`

## 📱 Usage

### For Recruiters:
1. Register with role "Recruiter"
2. Create a new job by pasting the job description
3. AI will parse skills and generate questions automatically
4. View leaderboard to see candidate rankings

### For Candidates:
1. Register with role "Candidate"
2. Browse available assessments
3. Start assessment and answer questions
4. Submit and view detailed results with AI feedback

## 🌐 Access

- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## 📊 Demo Workflow

1. **Create Job** (Recruiter)
   - Title: "Full Stack Developer"
   - Description: Paste job description
   - AI generates 10 MCQ + 5 Subjective + 3 Coding questions

2. **Take Assessment** (Candidate)
   - Answer questions
   - Code is executed automatically
   - Subjective answers evaluated by AI

3. **View Results**
   - Overall score and ranking
   - Skill-wise breakdown
   - Strengths, weaknesses, skill gaps
   - AI-generated recommendations

## 🏗️ Architecture

```
Backend (FastAPI + Python)
├── Gemini API Integration
├── SQLite Database
├── Code Execution Engine
├── Plagiarism Detector
└── Anomaly Detection

Frontend (React + Vite)
├── Recruiter Dashboard
├── Candidate Dashboard
├── Assessment Interface
├── Results & Analytics
└── Leaderboard
```

## 🔐 Security Features

- JWT Authentication
- Password hashing (bcrypt)
- Role-based access control
- SQL injection protection
- Code execution sandboxing

## 🐛 Troubleshooting

**Backend won't start:**
- Check if Python 3.8+ is installed
- Activate virtual environment
- Install requirements again

**Gemini API errors:**
- Verify API key in .env
- Check free tier quota
- Ensure internet connection

**Frontend errors:**
- Run `npm install` again
- Clear cache: `npm cache clean --force`
- Check Node.js version

## 📝 Project Structure

```
iitgandhi/
├── backend/
│   ├── main.py              # FastAPI app & routes
│   ├── models.py            # Database models
│   ├── schemas.py           # Pydantic schemas
│   ├── gemini_service.py    # AI integration
│   ├── assessment_utils.py  # Code execution & plagiarism
│   ├── auth.py              # Authentication
│   ├── database.py          # Database config
│   └── config.py            # Settings
│
├── frontend/
│   ├── src/
│   │   ├── pages/           # React pages
│   │   ├── components/      # React components
│   │   ├── api.js           # API calls
│   │   └── App.jsx          # Main app
│   └── package.json
│
├── README.md
├── QUICKSTART.md
├── setup.ps1
└── run.ps1
```

## 🎯 Key Endpoints

### Authentication
- `POST /register` - Register user
- `POST /token` - Login

### Jobs
- `POST /jobs` - Create job (with AI parsing)
- `GET /jobs` - List jobs
- `GET /jobs/{id}` - Get job details

### Assessments
- `POST /assessments` - Start assessment
- `GET /assessments/{id}/questions` - Get questions
- `POST /assessments/{id}/submit` - Submit answer
- `POST /assessments/{id}/complete` - Complete assessment

### Results
- `GET /assessments/{id}/results` - Get results
- `GET /jobs/{id}/leaderboard` - Get leaderboard

## 🤖 AI Features

1. **Job Description Parsing**
   - Extracts skills, experience level, role type
   - Identifies domain knowledge requirements

2. **Question Generation**
   - Context-aware questions based on JD
   - Balanced difficulty distribution
   - Aligned with required skills

3. **Subjective Evaluation**
   - Detailed feedback on answers
   - Score with justification
   - Identifies strengths/weaknesses

4. **Comprehensive Reports**
   - Overall performance analysis
   - Skill gap identification
   - Hiring recommendations

## 💡 Tips

- Use clear, detailed job descriptions for better AI parsing
- Gemini free tier gives 60 requests/minute (sufficient for hackathon)
- Test with sample JDs before actual use
- Keep assessment duration reasonable (45-90 min)

## 🎓 For Hackathon Demo

1. Create 2-3 sample jobs with different roles
2. Have test candidates complete assessments
3. Show leaderboard and detailed analytics
4. Demonstrate AI-generated insights
5. Highlight anti-fraud features

## 📞 Support

For issues or questions during the hackathon, check:
- Backend logs in terminal
- Browser console for frontend errors
- API documentation at /docs endpoint

Good luck with your hackathon! 🚀
