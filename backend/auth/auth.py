"""
Authentication Module
Handles user authentication, password hashing, and session management.
"""

import hashlib
import secrets
from datetime import datetime, timedelta
from typing import Optional, Dict

class AuthManager:
    """Manages user authentication and sessions."""
    
    def __init__(self, db):
        """
        Initialize authentication manager.
        
        Args:
            db: Database instance
        """
        self.db = db
        self.sessions = {}  # In-memory session storage (use Redis in production)
    
    def hash_password(self, password: str) -> str:
        """
        Hash a password using SHA-256 (simple hashing for student project).
        In production, use bcrypt or argon2.
        
        Args:
            password: Plain text password
            
        Returns:
            Hashed password
        """
        return hashlib.sha256(password.encode()).hexdigest()
    
    def verify_password(self, password: str, hashed: str) -> bool:
        """
        Verify a password against its hash.
        
        Args:
            password: Plain text password
            hashed: Hashed password
            
        Returns:
            True if password matches, False otherwise
        """
        return self.hash_password(password) == hashed
    
    def create_session(self, user_id: str, email: str) -> str:
        """
        Create a new session for a user.
        
        Args:
            user_id: User ID
            email: User email
            
        Returns:
            Session token
        """
        token = secrets.token_urlsafe(32)
        self.sessions[token] = {
            'user_id': user_id,
            'email': email,
            'created_at': datetime.now(),
            'expires_at': datetime.now() + timedelta(hours=24)
        }
        return token
    
    def validate_session(self, token: str) -> Optional[Dict]:
        """
        Validate a session token.
        
        Args:
            token: Session token
            
        Returns:
            Session data if valid, None otherwise
        """
        if token not in self.sessions:
            return None
        
        session = self.sessions[token]
        if datetime.now() > session['expires_at']:
            del self.sessions[token]
            return None
        
        return session
    
    def destroy_session(self, token: str):
        """
        Destroy a session.
        
        Args:
            token: Session token
        """
        if token in self.sessions:
            del self.sessions[token]
    
    def is_admin(self, email: str) -> bool:
        """
        Check if user is admin.
        
        Args:
            email: User email
            
        Returns:
            True if admin, False otherwise
        """
        return email == 'fayerakena@gmail.com'


