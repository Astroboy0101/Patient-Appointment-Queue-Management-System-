# Setup Checklist

Use this checklist to ensure everything is set up correctly.

## Pre-Setup

- [ ] Python 3.8+ installed
- [ ] Web browser installed
- [ ] Text editor/IDE ready
- [ ] (Optional) Supabase account created

## Backend Setup

- [ ] Navigate to `backend/` directory
- [ ] Create virtual environment: `python -m venv venv`
- [ ] Activate virtual environment
- [ ] Install dependencies: `pip install -r requirements.txt`
- [ ] Create `.env` file (optional for testing)
- [ ] Add Supabase credentials to `.env` (if using database)
- [ ] Run backend: `python app.py`
- [ ] Verify backend runs on `http://localhost:5000`
- [ ] Test health endpoint: `http://localhost:5000/api/health`

## Frontend Setup

- [ ] Navigate to `frontend/` directory
- [ ] Verify all HTML files exist
- [ ] Verify CSS file exists: `css/style.css`
- [ ] Verify JS files exist: `js/auth.js`, `js/api.js`, `js/theme.js`
- [ ] Check API_BASE_URL in `js/auth.js` and `js/api.js`
- [ ] Open `index.html` in browser or use local server
- [ ] Verify homepage loads correctly

## Database Setup (Optional)

- [ ] Create Supabase project
- [ ] Run SQL from `database/schema.sql`
- [ ] Verify tables created
- [ ] Verify example data inserted
- [ ] Update backend `.env` with credentials
- [ ] Test database connection

## Feature Testing

### Authentication
- [ ] Homepage accessible without login
- [ ] Sign up creates new account
- [ ] Login works with credentials
- [ ] Logout clears session
- [ ] Protected routes redirect to login
- [ ] Forgot password sends code
- [ ] Password reset works

### Patient Management
- [ ] Register new patient
- [ ] View patient list
- [ ] Search patients by name
- [ ] Patient data displays correctly

### Queue Management
- [ ] Add patient to regular queue
- [ ] Add patient to emergency queue
- [ ] View queue status
- [ ] Get next patient (dequeue)
- [ ] Emergency patients prioritized

### Scheduling
- [ ] Greedy algorithm assigns patients
- [ ] Workload balanced across doctors
- [ ] Emergency cases assigned first

### Admin
- [ ] Admin login works (fayerakena@gmail.com / dsa@project)
- [ ] Admin panel accessible
- [ ] Non-admin sees "Access Denied"
- [ ] Admin can view all data

### UI/UX
- [ ] Dark mode toggle works
- [ ] Light mode toggle works
- [ ] Theme persists across pages
- [ ] Responsive design works
- [ ] All buttons functional
- [ ] Error messages display
- [ ] Success messages display

## DSA Verification

- [ ] Queue operations work (enqueue/dequeue)
- [ ] Priority queue sorts correctly
- [ ] Linked list manages patients
- [ ] Greedy scheduler assigns optimally
- [ ] Code comments explain DSA concepts

## Documentation

- [ ] README.md complete
- [ ] DEPLOYMENT.md complete
- [ ] QUICKSTART.md complete
- [ ] Database README.md complete
- [ ] Code comments present

## Final Checks

- [ ] No console errors
- [ ] No linter errors
- [ ] All pages load correctly
- [ ] All features functional
- [ ] Example data displays
- [ ] Ready for submission

## Deployment (Optional)

- [ ] Backend deployed to Render/Railway
- [ ] Frontend deployed to Netlify/Vercel
- [ ] Database configured in Supabase
- [ ] API URLs updated in frontend
- [ ] CORS configured correctly
- [ ] Production testing complete

---

**Note**: System works without database for testing. Database is optional but recommended for full functionality.


