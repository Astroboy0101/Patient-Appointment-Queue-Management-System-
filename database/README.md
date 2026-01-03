# Database Setup Guide

## Why Supabase?

Supabase is chosen for this project because:

1. **Free Tier Available**: Perfect for student projects with generous free limits
2. **PostgreSQL-based**: Reliable, scalable, and industry-standard database
3. **Easy Integration**: Simple REST API and Python client library
4. **Built-in Features**: Authentication, real-time subscriptions, and storage
5. **Simple Setup**: No complex configuration needed
6. **Web Dashboard**: Easy database management through web interface

## Setup Steps

### 1. Create Supabase Account

1. Go to [https://supabase.com](https://supabase.com)
2. Sign up for a free account
3. Create a new project

### 2. Get Credentials

1. Go to Project Settings → API
2. Copy your:
   - Project URL (SUPABASE_URL)
   - Anon/Public Key (SUPABASE_KEY)

### 3. Run SQL Schema

1. Go to SQL Editor in Supabase dashboard
2. Copy and paste the contents of `schema.sql`
3. Run the SQL script to create tables and insert data

### 4. Configure Backend

1. Create a `.env` file in the `backend/` directory
2. Add your credentials:

```
SUPABASE_URL=your_project_url_here
SUPABASE_KEY=your_anon_key_here
SECRET_KEY=your_secret_key_here
```

### 5. Verify Setup

1. Check that all tables are created
2. Verify that doctor and patient data is inserted
3. Test the connection from the backend

## Database Tables

- **users**: User accounts and authentication
- **doctors**: Doctor information
- **patients**: Patient records
- **appointments**: Scheduled appointments
- **queue**: Regular patient queue
- **emergency_queue**: Emergency patient queue with priorities

## Notes

- The schema includes indexes for better query performance
- Fixed example data is inserted automatically
- All timestamps are automatically managed
- Foreign key constraints ensure data integrity


