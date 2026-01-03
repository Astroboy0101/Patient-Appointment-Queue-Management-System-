"""
Database Configuration and Setup
Uses Supabase as the database backend.

Why Supabase?
- Free tier available for student projects
- PostgreSQL-based (reliable and scalable)
- Easy REST API integration
- Built-in authentication support
- Real-time capabilities
- Simple setup and management
"""

import os
from dotenv import load_dotenv
from supabase import create_client, Client
from typing import Optional

load_dotenv()

class Database:
    """Database connection and operations manager."""
    
    def __init__(self):
        """Initialize database connection."""
        # Supabase configuration
        # These should be set as environment variables in production
        # Change these lines in database.py
        self.url = os.getenv('SUPABASE_URL')
        self.key = os.getenv('SUPABASE_KEY')
        if self.url and self.key:
            self.supabase: Optional[Client] = create_client(self.url, self.key)
        else:
            self.supabase = None
            print("Warning: Supabase credentials not set. Using mock data.")
    
    def get_client(self):
        """Get Supabase client."""
        return self.supabase
    
    def test_connection(self):
        """Test database connection."""
        if not self.supabase:
            return False
        try:
            # Simple test query
            result = self.supabase.table('users').select('id').limit(1).execute()
            return True
        except Exception as e:
            print(f"Database connection error: {e}")
            return False

# Initialize database instance
db = Database()

# This part only runs if you play this file directly
if __name__ == "__main__":
    print("--- Testing Connection ---")
    if db.test_connection():
        print("[SUCCESS] Your backend is talking to Supabase.")
        
        # Optional: Try to fetch doctors to be 100% sure
        client = db.get_client()
        try:
            doctors = client.table('doctors').select('*').execute()
            print(f"[SUCCESS] Found {len(doctors.data)} doctors in the database.")
        except Exception as e:
            print(f"[ERROR] Could not fetch data: {e}")
    else:
        print("[WARNING] Connection failed. Check your .env file credentials.")


