# Quick Start Guide - One Command Startup

## 🚀 How to Run the Application

### Windows Users (Easiest Method)

**Simply double-click:** `RUN.bat`

That's it! The script will:
1. ✅ Check Python installation
2. ✅ Setup virtual environment (if needed)
3. ✅ Install dependencies
4. ✅ Test database connection
5. ✅ Test DSA modules
6. ✅ Test Railway backend
7. ✅ Open frontend in browser

### Alternative Methods

#### Method 1: PowerShell Script
```powershell
.\start.ps1
```

#### Method 2: Batch File
```batch
start.bat
```

#### Method 3: Manual Start
1. Open terminal in project folder
2. Run: `.\RUN.bat`

---

## 📋 System Configuration

- **Backend**: Railway (https://web-production-d92ae.up.railway.app)
- **Database**: Supabase (Connected)
- **Frontend**: Local (Opens in browser)

---

## ⚠️ Important Notes

### Railway Free Tier
- Railway may sleep after 15 minutes of inactivity
- First request after sleep may take 30-60 seconds
- This is normal for free tier hosting

### If Backend is Sleeping
1. Wait 30-60 seconds for first request
2. Or visit: https://web-production-d92ae.up.railway.app/api/health
3. This will wake up the backend

---

## 🧪 Testing the System

After running `RUN.bat`, you can test:

1. **Health Check**: https://web-production-d92ae.up.railway.app/api/health
2. **Doctors API**: https://web-production-d92ae.up.railway.app/api/doctors
3. **Frontend**: Opens automatically in browser

---

## 🐛 Troubleshooting

### Python Not Found
- Install Python 3.8+ from python.org
- Make sure Python is added to PATH

### Dependencies Not Installing
- Check internet connection
- Run manually: `cd backend && pip install -r requirements.txt`

### Railway Backend Not Responding
- Wait 30-60 seconds (may be sleeping)
- Check Railway dashboard for service status
- Verify environment variables are set

### Frontend Not Opening
- Manually open: `frontend/index.html`
- Or use a local server: `python -m http.server 8000`

---

## ✅ Success Indicators

When everything is working, you should see:
- ✅ Database connected
- ✅ DSA modules working
- ✅ Railway backend accessible
- ✅ Frontend opened in browser

---

**That's it! Just double-click `RUN.bat` and you're ready to go!** 🎉


