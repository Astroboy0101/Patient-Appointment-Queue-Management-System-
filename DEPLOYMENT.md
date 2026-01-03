# Deployment Guide

This guide will help you deploy the Patient Appointment & Queue Management System to production.

## Prerequisites

- GitHub account
- Supabase account (free tier)
- Netlify/Vercel account (for frontend)
- Render/Railway account (for backend)

## Step 1: Database Setup (Supabase)

1. **Create Supabase Project**
   - Go to [supabase.com](https://supabase.com)
   - Sign up or log in
   - Click "New Project"
   - Fill in project details
   - Wait for project to be created

2. **Run Database Schema**
   - Go to SQL Editor in Supabase dashboard
   - Copy contents of `database/schema.sql`
   - Paste and run the SQL script
   - Verify tables are created

3. **Get Credentials**
   - Go to Project Settings → API
   - Copy:
     - Project URL (SUPABASE_URL)
     - Anon/Public Key (SUPABASE_KEY)
   - Save these for backend configuration

## Step 2: Backend Deployment (Render)

### Option A: Render

1. **Create Account**
   - Go to [render.com](https://render.com)
   - Sign up with GitHub

2. **Create Web Service**
   - Click "New" → "Web Service"
   - Connect your GitHub repository
   - Select the repository

3. **Configure Service**
   - **Name**: `patient-queue-backend`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
   - **Root Directory**: `backend`

4. **Add Environment Variables**
   - Click "Environment" tab
   - Add:
     - `SUPABASE_URL`: Your Supabase URL
     - `SUPABASE_KEY`: Your Supabase key
     - `SECRET_KEY`: Generate a random secret key
   - Click "Save Changes"

5. **Deploy**
   - Click "Create Web Service"
   - Wait for deployment to complete
   - Note the service URL (e.g., `https://patient-queue-backend.onrender.com`)

### Option B: Railway

1. **Create Account**
   - Go to [railway.app](https://railway.app)
   - Sign up with GitHub

2. **Create Project**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Select your repository

3. **Configure Service**
   - Railway will auto-detect Python
   - Set root directory to `backend`
   - Add environment variables:
     - `SUPABASE_URL`
     - `SUPABASE_KEY`
     - `SECRET_KEY`

4. **Deploy**
   - Railway will automatically deploy
   - Note the service URL

## Step 3: Frontend Deployment (Netlify)

1. **Create Account**
   - Go to [netlify.com](https://netlify.com)
   - Sign up with GitHub

2. **Create New Site**
   - Click "Add new site" → "Import an existing project"
   - Connect GitHub repository

3. **Configure Build Settings**
   - **Base directory**: `frontend`
   - **Build command**: (leave empty - static site)
   - **Publish directory**: `frontend`

4. **Update API URL**
   - After deployment, note your backend URL
   - Go to Site settings → Build & deploy → Environment
   - Or update directly in code:
     - Edit `frontend/js/auth.js`
     - Edit `frontend/js/api.js`
     - Change `API_BASE_URL` to your backend URL
   - Redeploy

5. **Deploy**
   - Click "Deploy site"
   - Wait for deployment
   - Note your site URL

### Alternative: Vercel

1. **Create Account**
   - Go to [vercel.com](https://vercel.com)
   - Sign up with GitHub

2. **Import Project**
   - Click "Add New" → "Project"
   - Import your repository

3. **Configure**
   - **Root Directory**: `frontend`
   - **Framework Preset**: Other
   - **Build Command**: (none)
   - **Output Directory**: `frontend`

4. **Deploy**
   - Click "Deploy"
   - Update API URLs as needed

## Step 4: Update Frontend API URLs

After deploying backend, update frontend to point to the backend URL:

1. **Edit Files**:
   - `frontend/js/auth.js`
   - `frontend/js/api.js`

2. **Change**:
   ```javascript
   const API_BASE_URL = 'http://localhost:5000/api';
   ```
   To:
   ```javascript
   const API_BASE_URL = 'https://your-backend-url.onrender.com/api';
   ```

3. **Commit and Push**:
   ```bash
   git add frontend/js/auth.js frontend/js/api.js
   git commit -m "Update API URL for production"
   git push
   ```

4. **Redeploy Frontend** (if needed)

## Step 5: CORS Configuration

If you encounter CORS errors:

1. **Backend** (`backend/app.py`):
   ```python
   CORS(app, supports_credentials=True, origins=["https://your-frontend-url.netlify.app"])
   ```

2. **Or allow all origins** (for development):
   ```python
   CORS(app, supports_credentials=True, origins=["*"])
   ```

## Step 6: Environment Variables Summary

### Backend (.env or platform settings)
```
SUPABASE_URL=https://xxxxx.supabase.co
SUPABASE_KEY=your_anon_key_here
SECRET_KEY=your_random_secret_key
```

### Frontend (in code)
```javascript
const API_BASE_URL = 'https://your-backend-url.onrender.com/api';
```

## Step 7: Testing Deployment

1. **Test Frontend**
   - Visit your frontend URL
   - Try logging in
   - Test all features

2. **Test Backend**
   - Check backend health: `https://your-backend-url/api/health`
   - Should return: `{"status": "healthy"}`

3. **Test Database**
   - Verify data is accessible
   - Test patient registration
   - Test queue operations

## Troubleshooting

### Backend Not Starting
- Check environment variables are set
- Verify Python version (3.8+)
- Check build logs for errors

### CORS Errors
- Update CORS configuration in `app.py`
- Verify frontend URL is in allowed origins

### Database Connection Issues
- Verify Supabase credentials
- Check Supabase project is active
- Verify tables exist

### Frontend Not Loading
- Check API URL is correct
- Verify backend is running
- Check browser console for errors

## Production Checklist

- [ ] Database schema deployed
- [ ] Backend deployed and accessible
- [ ] Frontend deployed and accessible
- [ ] API URLs updated in frontend
- [ ] CORS configured correctly
- [ ] Environment variables set
- [ ] All features tested
- [ ] Admin access working
- [ ] Search functionality working
- [ ] Queue management working

## Free Tier Limits

### Supabase
- 500 MB database
- 2 GB bandwidth
- 50,000 monthly active users

### Render
- 750 hours/month free
- Sleeps after 15 minutes of inactivity
- Can be woken up on first request

### Netlify
- 100 GB bandwidth/month
- 300 build minutes/month
- Unlimited sites

### Vercel
- 100 GB bandwidth/month
- Unlimited deployments
- Serverless functions

## Support

If you encounter issues:
1. Check deployment logs
2. Verify all environment variables
3. Test locally first
4. Check service status pages

---

**Note**: Free tier services may have limitations. For production use, consider paid plans.


