# How RUN.bat Works - Complete Guide

## 🚀 What Happens When You Run RUN.bat

When you double-click `RUN.bat`, here's exactly what happens:

### Step 1: System Verification
- ✅ Checks if Python is installed
- ✅ Verifies virtual environment exists (creates if needed)
- ✅ Installs/updates all dependencies

### Step 2: Database & DSA Testing
- ✅ Tests Supabase database connection
- ✅ Tests all DSA modules (Queue, Priority Queue, Linked List, Scheduler)

### Step 3: Starting Servers
- ✅ **Backend Server**: Starts Flask on `http://localhost:5000`
  - Handles all API requests
  - Connects to Supabase database
  - Manages authentication, patients, queue, etc.
  
- ✅ **Frontend Server**: Starts HTTP server on `http://localhost:8000`
  - Serves all HTML pages
  - Automatically injects local API URLs (`api_local.js` and `auth_local.js`)
  - Fixes all navigation links to work properly

### Step 4: Browser Opens
- ✅ Automatically opens `http://localhost:8000/index.html` in your browser
- ✅ All pages are fully functional and connected to the backend

---

## 📁 File Structure

```
project/
├── RUN.bat                    # Main startup script (double-click this!)
├── start_server.py            # Python server that runs both frontend & backend
├── backend/
│   ├── app.py                 # Flask backend server
│   ├── database.py            # Database connection
│   └── venv/                  # Virtual environment
├── frontend/
│   ├── index.html             # Home page
│   ├── login.html             # Login page
│   ├── dashboard.html         # Dashboard
│   ├── js/
│   │   ├── api.js             # Railway API (production)
│   │   ├── api_local.js       # Localhost API (development) ⭐
│   │   ├── auth.js            # Railway auth (production)
│   │   └── auth_local.js      # Localhost auth (development) ⭐
```

**Key Files:**
- `api_local.js` and `auth_local.js` are automatically used when running locally
- The server script replaces `api.js` → `api_local.js` in HTML files
- This ensures frontend connects to `localhost:5000` instead of Railway

---

## 🔄 How Pages Connect

### Navigation Flow:
1. **Home** (`index.html`) → Click "Login" → **Login** (`login.html`)
2. **Login** → After login → **Dashboard** (`dashboard.html`)
3. **Dashboard** → Links to all other pages:
   - Patient Registration
   - Appointments & Queue
   - Search
   - Admin Panel
   - About Us

### API Connection:
- All pages use `api_local.js` and `auth_local.js` when running locally
- These files point to `http://localhost:5000/api`
- Backend server handles all API requests
- Database (Supabase) is connected and working

---

## 🎯 What Works

### ✅ Fully Functional Features:

1. **Authentication**
   - Sign Up → Creates account
   - Login → Authenticates user
   - Logout → Clears session
   - Forgot Password → Sends verification code

2. **Patient Management**
   - Register Patient → Adds to database
   - View Patients → Lists all patients
   - Search Patients → Real-time search

3. **Queue Management**
   - Add to Regular Queue → FIFO queue
   - Add to Emergency Queue → Priority queue
   - View Queue Status → See all patients
   - Get Next Patient → Dequeue operation

4. **Scheduling**
   - Greedy Algorithm → Assigns patients to doctors
   - Workload Balancing → Distributes evenly

5. **Admin Panel**
   - Access Control → Only admin email can access
   - System Statistics → View all data
   - Doctor Management → View all doctors

---

## 🔧 Technical Details

### Backend (Flask)
- **Port**: 5000
- **URL**: http://localhost:5000
- **API Base**: http://localhost:5000/api
- **Database**: Supabase (connected)
- **CORS**: Enabled for all origins

### Frontend (HTTP Server)
- **Port**: 8000
- **URL**: http://localhost:8000
- **Serves**: All HTML, CSS, JS files
- **Auto-injects**: Local API URLs

### Database (Supabase)
- **Connection**: Automatic via environment variables
- **Tables**: users, doctors, patients, appointments, queue, emergency_queue
- **Status**: Connected and working

---

## 🐛 Troubleshooting

### Backend Not Starting
- Check if port 5000 is available
- Verify virtual environment is activated
- Check `backend/requirements.txt` dependencies

### Frontend Not Loading
- Check if port 8000 is available
- Verify `start_server.py` is running
- Check browser console for errors

### Database Connection Failed
- Verify `.env` file has correct Supabase credentials
- Check Supabase project is active
- Run `python backend/database.py` to test

### Pages Not Connecting
- Make sure both servers are running
- Check browser console for API errors
- Verify `api_local.js` and `auth_local.js` are loaded

---

## ✅ Success Indicators

When everything is working, you should see:

1. **Two Console Windows**:
   - Backend Server (Flask) - showing API requests
   - Frontend Server (HTTP) - serving pages

2. **Browser Opens**:
   - URL: `http://localhost:8000/index.html`
   - Home page loads correctly

3. **All Features Work**:
   - Can sign up and login
   - Can register patients
   - Can add to queue
   - Can search patients
   - Admin panel accessible (with admin credentials)

---

## 🎉 You're All Set!

**Just double-click `RUN.bat` and everything will start automatically!**

- Backend server starts
- Frontend server starts  
- Database connects
- Browser opens
- All pages work together
- Full functionality available

**No manual configuration needed - it's all automated!** 🚀


