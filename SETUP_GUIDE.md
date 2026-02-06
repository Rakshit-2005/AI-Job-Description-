# AI-Enabled Assessment Platform - Setup Guide

## Complete Step-by-Step Instructions

---

## 📋 Prerequisites

Before starting, make sure you have:
- ✅ Python 3.8 or higher installed
- ✅ Node.js (version 16+) installed
- ✅ PowerShell (comes with Windows)
- ✅ Internet connection

---

## 🚀 Step 1: Get Your Gemini API Key

### Option A: Automatic (Recommended)

Open PowerShell in the project folder and run:

```powershell
.\get-api-key.ps1
```

**What this does:**
1. Opens Google AI Studio in your browser
2. Guides you through getting the API key
3. Automatically saves it to the correct file

**Follow the prompts:**
- The browser will open to: https://aistudio.google.com/app/apikey
- Sign in with your Google account
- Click **"Create API Key"** button
- Copy the generated key
- Return to PowerShell and paste the key when asked
- Press Enter

✅ **Done!** Your API key is saved.

---

### Option B: Manual

If you prefer to do it manually:

1. **Visit:** https://aistudio.google.com/app/apikey
2. **Sign in** with your Google account
3. Click **"Create API Key"**
4. **Copy** the generated API key
5. Save it somewhere safe (you'll need it in Step 3)

---

## 🔧 Step 2: Install All Dependencies

Run this command in PowerShell (from project folder):

```powershell
.\setup.ps1
```

### What this script does:

**Backend Setup:**
- Creates a Python virtual environment
- Installs all Python packages (FastAPI, SQLAlchemy, etc.)
- Creates a `.env` file from the template

**Frontend Setup:**
- Installs all npm packages (React, Vite, etc.)

**Expected Output:**
```
Setting up Backend...
Creating virtual environment...
Installing Python dependencies...
Setting up Frontend...
Installing npm dependencies...
✅ Setup Complete!
```

⏱️ **Time:** 2-5 minutes (depending on internet speed)

---

## 🔑 Step 3: Configure Your API Key

### If you used `get-api-key.ps1` (Option A):
✅ **Skip this step** - your API key is already configured!

### If you did it manually (Option B):

1. **Navigate to:** `backend` folder
2. **Open file:** `.env` (not `.env.example`)
3. **Find the line:**
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   ```
4. **Replace with your actual key:**
   ```
   GEMINI_API_KEY=AIzaSyAbC123dEf456GhI789jKl...
   ```
5. **Add a secret key** (any random string):
   ```
   SECRET_KEY=my_super_secret_random_string_12345
   ```
6. **Save the file**

### Complete `.env` file should look like:
```
GEMINI_API_KEY=your_actual_gemini_key_here
DATABASE_URL=sqlite:///./assessment.db
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## ▶️ Step 4: Run the Application

Run this command in PowerShell:

```powershell
.\run.ps1
```

### What happens:
- **Two PowerShell windows will open:**
  - Window 1: Backend server (Python/FastAPI)
  - Window 2: Frontend server (React/Vite)

### Expected Output:

**Backend Window:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete.
```

**Frontend Window:**
```
VITE v5.x.x  ready in xxx ms

➜  Local:   http://localhost:5173/
➜  Network: use --host to expose
```

✅ **Both servers are now running!**

---

## 🌐 Step 5: Access the Application

Open your web browser and navigate to:

```
http://localhost:5173
```

### Available URLs:

| Service | URL | Description |
|---------|-----|-------------|
| **Frontend** | http://localhost:5173 | Main application UI |
| **Backend API** | http://localhost:8000 | API endpoints |
| **API Docs** | http://localhost:8000/docs | Interactive API documentation |
| **Database** | `backend/assessment.db` | SQLite database file |

---

## ✅ Verify Everything Works

### 1. Check Frontend
- Open: http://localhost:5173
- You should see the login/register page
- Try creating an account

### 2. Check Backend
- Open: http://localhost:8000/docs
- You should see the FastAPI documentation
- API endpoints should be listed

### 3. Test the Application
- **Register** as a recruiter
- **Create** a job description
- **Generate** assessment questions
- Verify that Gemini AI is working

---

## 🛑 How to Stop the Application

To stop the servers:

1. Go to each PowerShell window (backend and frontend)
2. Press `Ctrl + C`
3. Type `Y` if asked to terminate
4. Close the windows

---

## 🔄 How to Start Again

Next time you want to run the application:

```powershell
.\run.ps1
```

That's it! No need to run setup again.

---

## 📁 Important Files & Folders

### Files You Need to Know:

| File/Folder | Purpose | Do You Edit? |
|-------------|---------|--------------|
| `backend\.env` | Contains your API key | ✅ YES (one time) |
| `backend\.env.example` | Template file | ❌ NO (just a reference) |
| `setup.ps1` | Initial setup script | ❌ NO |
| `run.ps1` | Start servers script | ❌ NO |
| `get-api-key.ps1` | Get API key helper | ❌ NO |

### Project Structure:
```
iitgandhi/
├── backend/              # Python (FastAPI) backend
│   ├── .env             # 🔑 Your API key HERE
│   ├── main.py          # Backend entry point
│   └── requirements.txt # Python dependencies
├── frontend/            # React frontend
│   ├── src/            # React components
│   └── package.json    # npm dependencies
├── setup.ps1           # Setup script
├── run.ps1             # Run script
└── get-api-key.ps1     # API key helper
```

---

## 🆘 Troubleshooting

### Problem: "Command not found: python"
**Solution:** Install Python from https://www.python.org/downloads/
- Make sure to check "Add Python to PATH" during installation

### Problem: "Command not found: npm"
**Solution:** Install Node.js from https://nodejs.org/
- Download the LTS (Long Term Support) version

### Problem: Backend fails to start
**Solution:** 
1. Check if `.env` file exists in `backend` folder
2. Verify your `GEMINI_API_KEY` is correct
3. Make sure Python virtual environment is activated

### Problem: Frontend shows network error
**Solution:** 
1. Make sure backend is running (check http://localhost:8000/docs)
2. Check if both servers are running in separate windows

### Problem: "Module not found" errors
**Solution:** Run setup again:
```powershell
.\setup.ps1
```

### Problem: Port 8000 or 5173 already in use
**Solution:** 
1. Close any other applications using these ports
2. Or stop the existing servers with `Ctrl + C`

---

## 📞 Quick Reference Commands

```powershell
# First time setup
.\get-api-key.ps1    # Get your Gemini API key
.\setup.ps1          # Install everything

# Every time you want to run
.\run.ps1            # Start both servers

# Testing
.\test.ps1           # Run tests (if available)
```

---

## 🎯 Summary: What You Actually Need to Change

**Only ONE file needs your Gemini API key:**

📄 **`backend\.env`**

That's it! Everything else is automatic.

---

## 📧 Support

If you encounter issues:
1. Check the Troubleshooting section above
2. Verify all prerequisites are installed
3. Ensure your Gemini API key is valid
4. Check that both servers are running

---

## 🎉 Success Checklist

- ✅ Obtained Gemini API key
- ✅ Ran `setup.ps1` successfully
- ✅ Configured `backend\.env` file
- ✅ Ran `run.ps1` - both servers started
- ✅ Opened http://localhost:5173 in browser
- ✅ Application loaded successfully

---

**Generated:** February 2026
**Version:** 1.0
**Platform:** AI-Enabled Intelligent Assessment & Hiring Platform
