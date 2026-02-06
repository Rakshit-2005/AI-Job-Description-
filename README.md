# AI-Enabled Intelligent Assessment & Hiring Platform

## Tech Stack
- **Backend**: Python + FastAPI
- **Frontend**: React + Vite
- **Database**: SQLite (development) / PostgreSQL (production)
- **AI**: Google Gemini API
- **Code Execution**: Docker (optional) / subprocess

## Setup Instructions

### Backend Setup
```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### Frontend Setup
```bash
cd frontend
npm install
```

### Environment Variables
Create `.env` file in backend directory:
```
GEMINI_API_KEY=your_api_key_here
DATABASE_URL=sqlite:///./assessment.db
SECRET_KEY=your_secret_key
```

### Run Application
```bash
# Backend (from backend directory)
uvicorn main:app --reload

# Frontend (from frontend directory)
npm run dev
```

## Features
- ✅ JD Parsing with Gemini
- ✅ Automated Question Generation
- ✅ Multi-format Assessments (MCQ, Subjective, Coding)
- ✅ AI-powered Evaluation
- ✅ Plagiarism Detection
- ✅ Ranking & Leaderboards
- ✅ Detailed Analytics
