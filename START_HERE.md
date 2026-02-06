# 🚀 GETTING STARTED - Your Next Steps

Welcome! Your AI Assessment Platform is ready. Follow these steps to get it running.

---

## ⚡ Quick Start (5 Minutes)

### Step 1: Get Gemini API Key (2 min)
```powershell
.\get-api-key.ps1
```
This will:
- Open Google AI Studio in your browser
- Guide you to create a FREE API key
- Automatically save it to your configuration

---

### Step 2: Install Dependencies (2 min)
```powershell
.\setup.ps1
```
This will:
- Create Python virtual environment
- Install all Python packages
- Install all Node.js packages
- Set up configuration files

---

### Step 3: Start the Application (1 min)
```powershell
.\run.ps1
```
This will:
- Start backend server on port 8000
- Start frontend server on port 5173
- Open two terminal windows

---

## 🌐 Access Your Application

Once running, open these URLs:

- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

---

## 🎯 First Time Usage

### Create Your First Job (As Recruiter)

1. Go to http://localhost:5173
2. Click **Register**
3. Fill in:
   - Full Name: Your Name
   - Email: recruiter@test.com
   - Password: test123
   - Role: **Recruiter**
4. Click **Register**
5. Click **+ Create New Job**
6. Fill in:
   - Title: "Full Stack Developer"
   - Description: Copy from `SAMPLE_DATA.md` file
   - Duration: 60 minutes
   - Cutoff: 60%
7. Click **Create Job**
8. Wait 10-15 seconds for AI to generate questions
9. Success! Job created with auto-generated questions

### Take Your First Assessment (As Candidate)

1. **Logout** (click Logout button)
2. Click **Register** again
3. Fill in:
   - Full Name: Test Candidate
   - Email: candidate@test.com
   - Password: test123
   - Role: **Candidate**
4. Click **Register**
5. You'll see available assessments
6. Click **Start Assessment**
7. Answer questions:
   - MCQ: Select an option
   - Subjective: Write your answer
   - Coding: Write code solution
8. Click **Next** after each question
9. On last question, click **Submit & Complete**
10. View your detailed results!

### View Leaderboard

1. Logout and login as recruiter again
2. In your dashboard, click **View Leaderboard**
3. See all candidates ranked by score
4. View detailed analytics

---

## 📁 Project Structure Quick Reference

```
iitgandhi/
├── backend/          → Python FastAPI backend
├── frontend/         → React frontend
├── *.ps1            → Setup/run scripts
├── *.md             → Documentation
└── .gitignore       → Git ignore rules
```

---

## 🔧 Troubleshooting

### Backend won't start
```powershell
cd backend
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

### Frontend won't start
```powershell
cd frontend
npm install
npm run dev
```

### "Module not found" errors
```powershell
# Backend
cd backend
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt

# Frontend
cd frontend
rm -rf node_modules
npm install
```

### Gemini API errors
1. Check your API key in `backend\.env`
2. Make sure it starts with `GEMINI_API_KEY=`
3. No quotes around the key
4. Key should be ~40 characters

### Database errors
```powershell
# Delete and recreate database
cd backend
rm assessment.db  # if it exists
python -c "from database import Base, engine; Base.metadata.create_all(bind=engine)"
```

---

## 🧪 Testing the Platform

Run the test script to check everything:
```powershell
.\test.ps1
```

This will verify:
- ✅ Python installed
- ✅ Node.js installed
- ✅ Dependencies installed
- ✅ API key configured
- ✅ Backend running
- ✅ Frontend running

---

## 📚 Documentation Files

- **README.md** - Project overview
- **QUICKSTART.md** - Detailed setup instructions
- **DOCUMENTATION.md** - Complete technical docs
- **PROJECT_SUMMARY.md** - Features and highlights
- **SAMPLE_DATA.md** - Test data and examples
- **UI_GUIDE.md** - UI/UX design guide

---

## 🎬 Demo Preparation

### For Hackathon Presentation:

1. **Prepare 2 browsers/incognito windows:**
   - Window 1: Recruiter account
   - Window 2: Candidate account

2. **Before presentation:**
   - Start both servers
   - Create 1-2 sample jobs
   - Keep SAMPLE_DATA.md open for copy-paste

3. **During presentation:**
   - Show recruiter creating job (paste JD)
   - Show AI generating questions
   - Switch to candidate view
   - Take partial assessment
   - Show results and leaderboard

4. **Highlight these features:**
   - AI-powered question generation
   - Real-time code execution
   - Plagiarism detection
   - Comprehensive analytics
   - Beautiful UI

---

## 💡 Pro Tips

1. **Use SAMPLE_DATA.md** - Contains ready-to-use job descriptions
2. **Check API Docs** - Visit /docs endpoint for Swagger UI
3. **Monitor logs** - Watch terminal for errors
4. **Test incrementally** - Create job → Take assessment → View results
5. **Keep API key safe** - Don't commit .env to git

---

## 🎯 Key Features to Demo

1. ✅ **AI Parsing** - Show how JD is automatically analyzed
2. ✅ **Question Types** - MCQ, Subjective, Coding
3. ✅ **Auto Evaluation** - Instant scoring
4. ✅ **Code Execution** - Real Python code testing
5. ✅ **Detailed Reports** - Strengths, weaknesses, gaps
6. ✅ **Leaderboard** - Real-time rankings
7. ✅ **Anti-Fraud** - Plagiarism and anomaly detection

---

## 🆘 Need Help?

### Check These First:
1. Run `.\test.ps1` to diagnose issues
2. Check terminal logs for errors
3. Verify API key in backend\.env
4. Make sure ports 8000 and 5173 are free

### Common Issues:
- **Port in use**: Close other applications using ports 8000/5173
- **API errors**: Check internet connection and API key
- **Import errors**: Reinstall dependencies

---

## 📞 System Requirements

**Minimum:**
- Windows 10+
- Python 3.8+
- Node.js 16+
- 4GB RAM
- Internet connection (for Gemini API)

**Recommended:**
- Windows 11
- Python 3.10+
- Node.js 18+
- 8GB RAM
- Stable internet

---

## ✨ You're All Set!

Your AI Assessment Platform is ready to use. Follow the steps above and you'll be running in minutes.

**Next command to run:**
```powershell
.\get-api-key.ps1
```

Then:
```powershell
.\setup.ps1
```

Then:
```powershell
.\run.ps1
```

**That's it! Good luck with your hackathon! 🚀**

---

Made with ❤️ for IIT Gandhinagar Hackathon
