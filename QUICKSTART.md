# Quick Start Guide

Get the Patient Appointment & Queue Management System running in 5 minutes!

## Prerequisites

- Python 3.8 or higher
- Web browser
- (Optional) Supabase account for database

## Step 1: Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file (optional - works without database for testing)
# Copy .env.example and add your Supabase credentials

# Run the server
python app.py
```

Backend will run on `http://localhost:5000`

## Step 2: Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Option 1: Open directly in browser
# Just open index.html in your browser

# Option 2: Use a local server (recommended)
# Using Python:
python -m http.server 8000

# Using Node.js:
npx http-server
```

Frontend will be available at `http://localhost:8000` (or the port you chose)

## Step 3: Test the Application

1. Open frontend in browser
2. Click "Sign Up" to create an account
3. Login with your credentials
4. Try registering a patient
5. Add patient to queue
6. Test the greedy scheduler

## Admin Access

- Email: `fayerakena@gmail.com`
- Password: `dsa@project`

## Troubleshooting

### Backend won't start
- Check if port 5000 is available
- Verify Python version: `python --version`
- Check if dependencies installed: `pip list`

### Frontend can't connect to backend
- Verify backend is running
- Check API_BASE_URL in `frontend/js/auth.js` and `frontend/js/api.js`
- Check browser console for errors

### Database connection issues
- System works without database (uses in-memory data)
- For full functionality, set up Supabase (see `database/README.md`)

## Next Steps

- See `README.md` for full documentation
- See `DEPLOYMENT.md` for production deployment
- See `database/README.md` for database setup

## Features to Test

1. ✅ User registration and login
2. ✅ Patient registration
3. ✅ Add to queue (regular and emergency)
4. ✅ View queue status
5. ✅ Greedy scheduling algorithm
6. ✅ Search patients
7. ✅ Admin panel (with admin credentials)
8. ✅ Dark/Light mode toggle

Enjoy exploring the DSA concepts in action! 🚀


