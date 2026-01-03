-- Patient Appointment & Queue Management System
-- Database Schema for Supabase (PostgreSQL)

-- Users Table
CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    name VARCHAR(255),
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Doctors Table
CREATE TABLE IF NOT EXISTS doctors (
    id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    specialization VARCHAR(255),
    available BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Patients Table
CREATE TABLE IF NOT EXISTS patients (
    id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INTEGER,
    phone VARCHAR(20),
    email VARCHAR(255),
    condition TEXT,
    is_emergency BOOLEAN DEFAULT FALSE,
    priority INTEGER DEFAULT 5,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Appointments Table
CREATE TABLE IF NOT EXISTS appointments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    patient_id VARCHAR(50) REFERENCES patients(id),
    doctor_id VARCHAR(50) REFERENCES doctors(id),
    appointment_date TIMESTAMP,
    status VARCHAR(50) DEFAULT 'scheduled',
    created_at TIMESTAMP DEFAULT NOW()
);

-- Queue Table (Regular Queue)
CREATE TABLE IF NOT EXISTS queue (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    patient_id VARCHAR(50) REFERENCES patients(id),
    added_at TIMESTAMP DEFAULT NOW(),
    status VARCHAR(50) DEFAULT 'waiting'
);

-- Emergency Queue Table (Priority Queue)
CREATE TABLE IF NOT EXISTS emergency_queue (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    patient_id VARCHAR(50) REFERENCES patients(id),
    priority INTEGER NOT NULL,
    added_at TIMESTAMP DEFAULT NOW(),
    status VARCHAR(50) DEFAULT 'waiting'
);

-- Indexes for better performance
CREATE INDEX IF NOT EXISTS idx_patients_name ON patients(name);
CREATE INDEX IF NOT EXISTS idx_queue_patient ON queue(patient_id);
CREATE INDEX IF NOT EXISTS idx_emergency_queue_priority ON emergency_queue(priority, added_at);
CREATE INDEX IF NOT EXISTS idx_appointments_patient ON appointments(patient_id);
CREATE INDEX IF NOT EXISTS idx_appointments_doctor ON appointments(doctor_id);

-- Insert Fixed Doctor Data
INSERT INTO doctors (id, name, specialization, available) VALUES
    ('ID-7149-16', 'Daniel Dea', 'General Medicine', TRUE),
    ('ID-5643-16', 'Kena Fayera', 'Cardiology', TRUE),
    ('ID-2905-16', 'Abdurahman Muktar', 'Pediatrics', TRUE),
    ('ID-7060-16', 'Abel Yeshewalem', 'Orthopedics', TRUE),
    ('ID-8338-16', 'Gersam Mussie', 'Neurology', TRUE),
    ('ID-8263-16', 'Leulekal Nahusenay', 'Emergency Medicine', TRUE)
ON CONFLICT (id) DO NOTHING;

-- Insert Fixed Patient Data
INSERT INTO patients (id, name, age, phone, email, condition, is_emergency, priority) VALUES
    ('P001', 'NAOL MULISA', 35, '0912345678', 'naol@example.com', 'Fever', FALSE, 5),
    ('P002', 'SEWYISHAL NETSANET', 28, '0912345679', 'sewyishal@example.com', 'Chest Pain', TRUE, 1),
    ('P003', 'Wirtu Borana', 42, '0912345680', 'wirtu@example.com', 'Headache', FALSE, 5),
    ('P004', 'YISAKOR TAMIRAT', 31, '0912345681', 'yisakor@example.com', 'Broken Arm', TRUE, 2),
    ('P005', 'Surafiel Nigus', 25, '0912345682', 'surafiel@example.com', 'Cold', FALSE, 5),
    ('P006', 'Semere Hailu', 50, '0912345683', 'semere@example.com', 'High Blood Pressure', FALSE, 5)
ON CONFLICT (id) DO NOTHING;


