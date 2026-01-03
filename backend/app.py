"""
Flask Application - Patient Appointment & Queue Management System
Main backend server with API endpoints.
"""

from flask import Flask, request, jsonify, session
from flask_cors import CORS
import os
from datetime import datetime
import uuid

from database import db
from auth.auth import AuthManager
from models.patient import Patient
from models.doctor import Doctor
from dsa.queue import Queue
from dsa.priority_queue import PriorityQueue
from dsa.linked_list import LinkedList
from dsa.scheduler import Scheduler

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'dsa-project-secret-key-change-in-production')
CORS(app, supports_credentials=True, origins=["*"])  # Allow all origins for development

# Initialize managers
auth_manager = AuthManager(db)

# Initialize DSA structures
patient_list = LinkedList()  # Dynamic patient records
regular_queue = Queue()  # Regular appointments
emergency_queue = PriorityQueue()  # Emergency cases

# Mock data for doctors (will be replaced with database)
DOCTORS = [
    {'id': 'ID-7149-16', 'name': 'Daniel Dea', 'specialization': 'General Medicine', 'available': True},
    {'id': 'ID-5643-16', 'name': 'Kena Fayera', 'specialization': 'Cardiology', 'available': True},
    {'id': 'ID-2905-16', 'name': 'Abdurahman Muktar', 'specialization': 'Pediatrics', 'available': True},
    {'id': 'ID-7060-16', 'name': 'Abel Yeshewalem', 'specialization': 'Orthopedics', 'available': True},
    {'id': 'ID-8338-16', 'name': 'Gersam Mussie', 'specialization': 'Neurology', 'available': True},
    {'id': 'ID-8263-16', 'name': 'Leulekal Nahusenay', 'specialization': 'Emergency Medicine', 'available': True}
]

# Mock patients (will be replaced with database)
MOCK_PATIENTS = [
    {'id': 'P001', 'name': 'NAOL MULISA', 'age': 35, 'phone': '0912345678', 'email': 'naol@example.com', 'condition': 'Fever', 'is_emergency': False, 'priority': 5},
    {'id': 'P002', 'name': 'SEWYISHAL NETSANET', 'age': 28, 'phone': '0912345679', 'email': 'sewyishal@example.com', 'condition': 'Chest Pain', 'is_emergency': True, 'priority': 1},
    {'id': 'P003', 'name': 'Wirtu Borana', 'age': 42, 'phone': '0912345680', 'email': 'wirtu@example.com', 'condition': 'Headache', 'is_emergency': False, 'priority': 5},
    {'id': 'P004', 'name': 'YISAKOR TAMIRAT', 'age': 31, 'phone': '0912345681', 'email': 'yisakor@example.com', 'condition': 'Broken Arm', 'is_emergency': True, 'priority': 2},
    {'id': 'P005', 'name': 'Surafiel Nigus', 'age': 25, 'phone': '0912345682', 'email': 'surafiel@example.com', 'condition': 'Cold', 'is_emergency': False, 'priority': 5},
    {'id': 'P006', 'name': 'Semere Hailu', 'age': 50, 'phone': '0912345683', 'email': 'semere@example.com', 'condition': 'High Blood Pressure', 'is_emergency': False, 'priority': 5}
]

# Initialize with mock data
for patient in MOCK_PATIENTS:
    patient_list.append(patient)

# Helper function to check authentication
def require_auth():
    """Check if user is authenticated."""
    token = request.headers.get('Authorization') or session.get('token')
    if not token:
        return None
    return auth_manager.validate_session(token.replace('Bearer ', ''))

# Helper function to check admin
def require_admin():
    """Check if user is admin."""
    token = request.headers.get('Authorization') or session.get('token')
    if not token:
        return None
    session_data = auth_manager.validate_session(token.replace('Bearer ', ''))
    if not session_data:
        return None
    return auth_manager.is_admin(session_data['email'])


# ==================== AUTHENTICATION ENDPOINTS ====================

@app.route('/api/auth/signup', methods=['POST'])
def signup():
    """User registration endpoint."""
    try:
        data = request.json
        email = data.get('email')
        password = data.get('password')
        name = data.get('name')
        
        if not email or not password:
            return jsonify({'error': 'Email and password required'}), 400
        
        # Hash password
        hashed_password = auth_manager.hash_password(password)
        
        # Save to database (mock for now)
        user_id = str(uuid.uuid4())
        
        # Create session
        token = auth_manager.create_session(user_id, email)
        session['token'] = token
        
        return jsonify({
            'message': 'User registered successfully',
            'token': token,
            'user': {'id': user_id, 'email': email, 'name': name}
        }), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/auth/login', methods=['POST'])
def login():
    """User login endpoint."""
    try:
        data = request.json
        email = data.get('email')
        password = data.get('password')
        
        if not email or not password:
            return jsonify({'error': 'Email and password required'}), 400
        
        # Check admin credentials
        if email == 'fayerakena@gmail.com' and password == 'dsa@project':
            user_id = 'admin-001'
            token = auth_manager.create_session(user_id, email)
            session['token'] = token
            return jsonify({
                'message': 'Login successful',
                'token': token,
                'user': {'id': user_id, 'email': email, 'is_admin': True}
            }), 200
        
        # For other users, check database (mock for now)
        # In real implementation, check database
        user_id = str(uuid.uuid4())
        token = auth_manager.create_session(user_id, email)
        session['token'] = token
        
        return jsonify({
            'message': 'Login successful',
            'token': token,
            'user': {'id': user_id, 'email': email, 'is_admin': False}
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/auth/logout', methods=['POST'])
def logout():
    """User logout endpoint."""
    try:
        token = request.headers.get('Authorization') or session.get('token')
        if token:
            auth_manager.destroy_session(token.replace('Bearer ', ''))
        session.clear()
        return jsonify({'message': 'Logout successful'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/auth/forgot-password', methods=['POST'])
def forgot_password():
    """Forgot password endpoint - sends verification code."""
    try:
        data = request.json
        email = data.get('email')
        
        if not email:
            return jsonify({'error': 'Email required'}), 400
        
        # Generate verification code (in production, send via email)
        verification_code = str(uuid.uuid4())[:6].upper()
        
        # Store code temporarily (use Redis in production)
        # For now, return code directly (in production, send via email service)
        
        return jsonify({
            'message': 'Verification code sent to email',
            'verification_code': verification_code  # Remove in production
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/auth/reset-password', methods=['POST'])
def reset_password():
    """Reset password endpoint - requires verification code."""
    try:
        data = request.json
        email = data.get('email')
        code = data.get('code')
        new_password = data.get('new_password')
        
        if not all([email, code, new_password]):
            return jsonify({'error': 'Email, code, and new password required'}), 400
        
        # Verify code (in production, check stored code)
        # For now, accept any code
        
        # Hash new password
        hashed_password = auth_manager.hash_password(new_password)
        
        # Update password in database (mock)
        
        return jsonify({'message': 'Password reset successful'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/auth/me', methods=['GET'])
def get_current_user():
    """Get current authenticated user."""
    session_data = require_auth()
    if not session_data:
        return jsonify({'error': 'Unauthorized'}), 401
    
    return jsonify({
        'user': {
            'id': session_data['user_id'],
            'email': session_data['email'],
            'is_admin': auth_manager.is_admin(session_data['email'])
        }
    }), 200


# ==================== PATIENT ENDPOINTS ====================

@app.route('/api/patients', methods=['GET'])
def get_patients():
    """Get all patients."""
    session_data = require_auth()
    if not session_data:
        return jsonify({'error': 'Unauthorized'}), 401
    
    patients = patient_list.display()
    return jsonify({'patients': patients}), 200

@app.route('/api/patients', methods=['POST'])
def create_patient():
    """Create a new patient."""
    session_data = require_auth()
    if not session_data:
        return jsonify({'error': 'Unauthorized'}), 401
    
    try:
        data = request.json
        patient_id = f"P{str(uuid.uuid4())[:3].upper()}"
        
        patient_data = {
            'id': patient_id,
            'name': data.get('name'),
            'age': data.get('age'),
            'phone': data.get('phone'),
            'email': data.get('email'),
            'condition': data.get('condition'),
            'is_emergency': data.get('is_emergency', False),
            'priority': data.get('priority', 5)
        }
        
        # Add to linked list
        patient_list.append(patient_data)
        
        return jsonify({'message': 'Patient created successfully', 'patient': patient_data}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/patients/<patient_id>', methods=['GET'])
def get_patient(patient_id):
    """Get a specific patient."""
    session_data = require_auth()
    if not session_data:
        return jsonify({'error': 'Unauthorized'}), 401
    
    patient = patient_list.find(patient_id)
    if not patient:
        return jsonify({'error': 'Patient not found'}), 404
    
    return jsonify({'patient': patient}), 200

@app.route('/api/patients/search', methods=['GET'])
def search_patients():
    """Search patients by name."""
    session_data = require_auth()
    if not session_data:
        return jsonify({'error': 'Unauthorized'}), 401
    
    query = request.args.get('q', '').lower()
    if not query:
        return jsonify({'patients': []}), 200
    
    all_patients = patient_list.display()
    results = [p for p in all_patients if query in p.get('name', '').lower()]
    
    return jsonify({'patients': results}), 200


# ==================== DOCTOR ENDPOINTS ====================

@app.route('/api/doctors', methods=['GET'])
def get_doctors():
    """Get all doctors."""
    return jsonify({'doctors': DOCTORS}), 200

@app.route('/api/doctors/<doctor_id>', methods=['GET'])
def get_doctor(doctor_id):
    """Get a specific doctor."""
    doctor = next((d for d in DOCTORS if d['id'] == doctor_id), None)
    if not doctor:
        return jsonify({'error': 'Doctor not found'}), 404
    return jsonify({'doctor': doctor}), 200


# ==================== QUEUE ENDPOINTS ====================

@app.route('/api/queue', methods=['GET'])
def get_queue():
    """Get current queue status."""
    session_data = require_auth()
    if not session_data:
        return jsonify({'error': 'Unauthorized'}), 401
    
    # Format emergency queue with priority information
    emergency_list = []
    for entry in emergency_queue.items:
        emergency_list.append({
            'item': entry['item'],
            'priority': entry['priority']
        })
    
    return jsonify({
        'regular_queue': regular_queue.display(),
        'emergency_queue': emergency_list,
        'regular_size': regular_queue.size(),
        'emergency_size': emergency_queue.size()
    }), 200

@app.route('/api/queue/add', methods=['POST'])
def add_to_queue():
    """Add patient to queue."""
    session_data = require_auth()
    if not session_data:
        return jsonify({'error': 'Unauthorized'}), 401
    
    try:
        data = request.json
        patient_id = data.get('patient_id')
        is_emergency = data.get('is_emergency', False)
        priority = data.get('priority', 5)
        
        patient = patient_list.find(patient_id)
        if not patient:
            return jsonify({'error': 'Patient not found'}), 404
        
        if is_emergency:
            emergency_queue.enqueue(patient, priority)
        else:
            regular_queue.enqueue(patient)
        
        return jsonify({'message': 'Patient added to queue'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/queue/next', methods=['POST'])
def get_next_patient():
    """Get next patient from queue (dequeue)."""
    session_data = require_auth()
    if not session_data:
        return jsonify({'error': 'Unauthorized'}), 401
    
    # Priority: emergency first, then regular
    if not emergency_queue.is_empty():
        patient = emergency_queue.dequeue()
        return jsonify({'patient': patient, 'queue_type': 'emergency'}), 200
    elif not regular_queue.is_empty():
        patient = regular_queue.dequeue()
        return jsonify({'patient': patient, 'queue_type': 'regular'}), 200
    else:
        return jsonify({'message': 'Queue is empty'}), 200


# ==================== SCHEDULER ENDPOINTS ====================

@app.route('/api/scheduler/assign', methods=['POST'])
def assign_patients():
    """Assign patients to doctors using greedy algorithm."""
    session_data = require_auth()
    if not session_data:
        return jsonify({'error': 'Unauthorized'}), 401
    
    try:
        scheduler = Scheduler(DOCTORS)
        
        # Add all patients from queues to scheduler
        for patient in regular_queue.display():
            scheduler.add_patient(patient, is_emergency=False)
        
        for entry in emergency_queue.items:
            scheduler.add_patient(entry['item'], is_emergency=True, priority=entry['priority'])
        
        # Run greedy assignment algorithm
        assignments = scheduler.assign_patients()
        
        return jsonify({
            'message': 'Patients assigned successfully',
            'assignments': assignments
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# ==================== DASHBOARD ENDPOINTS ====================

@app.route('/api/dashboard/stats', methods=['GET'])
def get_dashboard_stats():
    """Get dashboard statistics."""
    session_data = require_auth()
    if not session_data:
        return jsonify({'error': 'Unauthorized'}), 401
    
    stats = {
        'total_patients': patient_list.get_size(),
        'regular_queue_size': regular_queue.size(),
        'emergency_queue_size': emergency_queue.size(),
        'total_doctors': len(DOCTORS),
        'available_doctors': len([d for d in DOCTORS if d['available']])
    }
    
    return jsonify({'stats': stats}), 200


# ==================== ADMIN ENDPOINTS ====================

@app.route('/api/admin/access', methods=['GET'])
def check_admin_access():
    """Check if user has admin access."""
    is_admin = require_admin()
    if not is_admin:
        return jsonify({'error': 'Access Denied', 'has_access': False}), 403
    
    return jsonify({'message': 'Admin access granted', 'has_access': True}), 200


# ==================== HEALTH CHECK ====================

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({'status': 'healthy', 'message': 'API is running'}), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)

