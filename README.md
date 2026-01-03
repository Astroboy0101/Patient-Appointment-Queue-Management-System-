# Patient Appointment & Queue Management System

A complete web application for managing patient appointments and queues, implementing core Data Structures & Algorithms concepts.

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [DSA Concepts Implemented](#dsa-concepts-implemented)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Database Setup](#database-setup)
- [Deployment](#deployment)
- [Team](#team)

## 🎯 Project Overview

**Problem**: Hospitals face long waiting times because patients are handled manually without prioritizing urgent cases.

**Solution**: A digital queue system that registers patients, prioritizes emergency cases, and optimizes patient flow using DSA concepts.

## ✨ Features

- **User Authentication**: Sign up, login, logout, and password reset
- **Patient Registration**: Add new patients with emergency priority support
- **Queue Management**: Regular FIFO queue and priority queue for emergencies
- **Smart Scheduling**: Greedy algorithm for optimal doctor-patient assignment
- **Search Functionality**: Real-time patient search
- **Admin Panel**: Restricted access for system administration
- **Dashboard**: Statistics and quick actions
- **Dark/Light Mode**: Theme toggle for better user experience

## 🔹 DSA Concepts Implemented

### 1. Queue (FIFO)
**Location**: `backend/dsa/queue.py`

A simple First-In-First-Out queue for managing regular patient appointments.

**Operations**:
- `enqueue(item)`: Add patient to the rear
- `dequeue()`: Remove patient from the front
- `peek()`: View front patient without removing
- `is_empty()`: Check if queue is empty
- `size()`: Get queue size

**Usage**: Regular appointments are processed in the order they arrive.

### 2. Priority Queue
**Location**: `backend/dsa/priority_queue.py`

A priority queue for handling emergency cases. Lower priority number = higher priority (1 is highest, 5 is lowest).

**Operations**:
- `enqueue(item, priority)`: Add patient with priority level
- `dequeue()`: Remove highest priority patient
- Items are automatically sorted by priority

**Usage**: Emergency patients are always served before regular patients, with critical cases (priority 1) handled first.

### 3. Linked List
**Location**: `backend/dsa/linked_list.py`

A singly linked list for dynamic patient record management.

**Operations**:
- `append(data)`: Add patient to end
- `prepend(data)`: Add patient to beginning
- `remove(patient_id)`: Remove patient by ID
- `find(patient_id)`: Find patient by ID
- `display()`: Get all patients as list

**Usage**: Patient records are stored dynamically, allowing efficient addition and removal.

### 4. Greedy Scheduling Algorithm
**Location**: `backend/dsa/scheduler.py`

A greedy algorithm for assigning patients to doctors efficiently.

**Greedy Strategy**:
1. Always assign the highest priority patient first (emergency cases)
2. Assign to the doctor with the least current workload
3. This ensures urgent cases are handled quickly and workload is balanced

**Algorithm Steps**:
```python
1. Process all emergency patients first (sorted by priority)
2. For each patient, choose doctor with minimum workload
3. Then process regular patients
4. Balance workload across all doctors
```

**Why Greedy?**: At each step, we make the locally optimal choice (highest priority + least workload), which leads to a globally optimal solution for patient assignment.

## 📁 Project Structure

```
.
├── backend/
│   ├── app.py                 # Flask application
│   ├── database.py            # Database configuration
│   ├── requirements.txt       # Python dependencies
│   ├── auth/
│   │   └── auth.py           # Authentication module
│   ├── models/
│   │   ├── patient.py        # Patient model
│   │   └── doctor.py         # Doctor model
│   └── dsa/
│       ├── queue.py          # Queue implementation
│       ├── priority_queue.py # Priority queue implementation
│       ├── linked_list.py   # Linked list implementation
│       └── scheduler.py     # Greedy scheduler
├── frontend/
│   ├── index.html           # Home page
│   ├── login.html           # Login page
│   ├── signup.html          # Sign up page
│   ├── dashboard.html       # Dashboard
│   ├── patient-registration.html
│   ├── appointment.html    # Queue management
│   ├── search.html          # Search page
│   ├── admin.html          # Admin panel
│   ├── about.html          # About us
│   ├── css/
│   │   └── style.css       # Main stylesheet
│   └── js/
│       ├── auth.js         # Authentication utilities
│       ├── api.js          # API calls
│       └── theme.js        # Theme management
├── database/
│   ├── schema.sql          # Database schema
│   └── README.md           # Database setup guide
└── README.md               # This file
```

## 🚀 Installation

### Prerequisites

- Python 3.8+
- Node.js (for frontend, optional)
- Supabase account (free tier)

### Backend Setup

1. Navigate to backend directory:
```bash
cd backend
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file:
```env
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
SECRET_KEY=your_secret_key
```

5. Run the application:
```bash
python app.py
```

The backend will run on `http://localhost:5000`

### Frontend Setup

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Open `index.html` in a web browser, or use a local server:
```bash
# Using Python
python -m http.server 8000

# Using Node.js
npx http-server
```

3. Update API URL in `frontend/js/auth.js` and `frontend/js/api.js` if needed:
```javascript
const API_BASE_URL = 'http://localhost:5000/api';
```

## 💻 Usage

### Accessing the Application

1. Open the frontend in your browser
2. Homepage is publicly accessible
3. Click "Sign Up" to create an account
4. Login with your credentials

### Admin Access

- **Email**: `fayerakena@gmail.com`
- **Password**: `dsa@project`

### Key Features

1. **Register Patient**: Add new patients with optional emergency status
2. **Queue Management**: Add patients to regular or emergency queue
3. **Smart Assignment**: Use greedy algorithm to assign patients to doctors
4. **Search**: Find patients by name
5. **Dashboard**: View system statistics

## 🗄️ Database Setup

See `database/README.md` for detailed database setup instructions.

### Quick Setup

1. Create Supabase account
2. Create new project
3. Run SQL from `database/schema.sql` in Supabase SQL Editor
4. Get credentials and add to backend `.env` file

## 🌐 Deployment

### Frontend (Netlify/Vercel)

1. **Netlify**:
   - Connect GitHub repository
   - Set build command: (none needed for static site)
   - Set publish directory: `frontend`
   - Deploy

2. **Vercel**:
   - Import project
   - Set root directory: `frontend`
   - Deploy

### Backend (Render/Railway)

1. **Render**:
   - Create new Web Service
   - Connect repository
   - Set build command: `pip install -r requirements.txt`
   - Set start command: `python app.py`
   - Add environment variables

2. **Railway**:
   - Create new project
   - Deploy from GitHub
   - Add environment variables
   - Deploy

### Environment Variables

- `SUPABASE_URL`: Your Supabase project URL
- `SUPABASE_KEY`: Your Supabase anon key
- `SECRET_KEY`: Flask secret key

### Update Frontend API URL

After deploying backend, update `API_BASE_URL` in:
- `frontend/js/auth.js`
- `frontend/js/api.js`

## 👥 Team

**Biomedical Engineering Students - Addis Ababa University**

- **Daniel Dea** — UGR/7149/16
- **Kena Fayera** — UGR/5643/16
- **Abdurahman Muktar** — UGR/2905/16
- **Abel Yeshewalem** — UGR/7060/16
- **Gersam Mussie** — UGR/8338/16
- **Leulekal Nahusenay** — UGR/8263/16

**Submitted to**: Mr. Endashaw A.

## 📝 Fixed Example Data

### Doctors
- Daniel Dea — ID-7149-16
- Kena Fayera — ID-5643-16
- Abdurahman Muktar — ID-2905-16
- Abel Yeshewalem — ID-7060-16
- Gersam Mussie — ID-8338-16
- Leulekal Nahusenay — ID-8263-16

### Patients
- NAOL MULISA
- SEWYISHAL NETSANET
- Wirtu Borana
- YISAKOR TAMIRAT
- Surafiel Nigus
- Semere Hailu

## 🔒 Security Notes

- Password hashing using SHA-256 (for student project)
- Session-based authentication
- Admin access restricted to specific email
- Protected routes require authentication

**Note**: For production, use bcrypt or argon2 for password hashing and implement proper session management.

## 📚 DSA Explanation Summary

### Why These Data Structures?

1. **Queue**: Natural fit for appointment scheduling (FIFO)
2. **Priority Queue**: Essential for emergency case handling
3. **Linked List**: Dynamic patient record management
4. **Greedy Algorithm**: Efficient doctor-patient assignment

### Time Complexity

- Queue operations: O(1) for enqueue/dequeue
- Priority Queue: O(n log n) for insertion (sorted list)
- Linked List: O(n) for search, O(1) for insertion
- Greedy Scheduler: O(n log n) for sorting + O(n) for assignment

## 🐛 Troubleshooting

### Backend Issues

- Check if port 5000 is available
- Verify environment variables are set
- Check Supabase connection

### Frontend Issues

- Verify API_BASE_URL is correct
- Check browser console for errors
- Ensure backend is running

### Database Issues

- Verify Supabase credentials
- Check table creation in Supabase dashboard
- Ensure data is inserted correctly

## 📄 License

This project is created for educational purposes as part of a Data Structures & Algorithms course.

## 🙏 Support

Support the project: [Buy us a Coffee](https://buymeacoffee.com/fayerakenaf)

---

**Note**: This is a student project demonstrating DSA concepts. Code is kept simple and well-commented for educational purposes.


