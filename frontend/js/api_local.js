/**
 * API Utilities - LOCAL DEVELOPMENT VERSION
 * Handles all API calls to the backend
 * Uses localhost:5000 for local development
 */

const API_BASE_URL = 'http://localhost:5000/api';

// Get auth headers
function getAuthHeaders() {
    const token = window.auth?.getToken();
    return {
        'Content-Type': 'application/json',
        ...(token ? { 'Authorization': `Bearer ${token}` } : {})
    };
}

// API functions
const api = {
    // Patients
    getPatients: async () => {
        const response = await fetch(`${API_BASE_URL}/patients`, {
            headers: getAuthHeaders()
        });
        return response.json();
    },

    createPatient: async (patientData) => {
        const response = await fetch(`${API_BASE_URL}/patients`, {
            method: 'POST',
            headers: getAuthHeaders(),
            body: JSON.stringify(patientData)
        });
        return response.json();
    },

    getPatient: async (patientId) => {
        const response = await fetch(`${API_BASE_URL}/patients/${patientId}`, {
            headers: getAuthHeaders()
        });
        return response.json();
    },

    searchPatients: async (query) => {
        const response = await fetch(`${API_BASE_URL}/patients/search?q=${encodeURIComponent(query)}`, {
            headers: getAuthHeaders()
        });
        return response.json();
    },

    // Doctors
    getDoctors: async () => {
        const response = await fetch(`${API_BASE_URL}/doctors`);
        return response.json();
    },

    getDoctor: async (doctorId) => {
        const response = await fetch(`${API_BASE_URL}/doctors/${doctorId}`);
        return response.json();
    },

    // Queue
    getQueue: async () => {
        const response = await fetch(`${API_BASE_URL}/queue`, {
            headers: getAuthHeaders()
        });
        return response.json();
    },

    addToQueue: async (patientId, isEmergency = false, priority = 5) => {
        const response = await fetch(`${API_BASE_URL}/queue/add`, {
            method: 'POST',
            headers: getAuthHeaders(),
            body: JSON.stringify({ patient_id: patientId, is_emergency: isEmergency, priority })
        });
        return response.json();
    },

    getNextPatient: async () => {
        const response = await fetch(`${API_BASE_URL}/queue/next`, {
            method: 'POST',
            headers: getAuthHeaders()
        });
        return response.json();
    },

    // Scheduler
    assignPatients: async () => {
        const response = await fetch(`${API_BASE_URL}/scheduler/assign`, {
            method: 'POST',
            headers: getAuthHeaders()
        });
        return response.json();
    },

    // Dashboard
    getDashboardStats: async () => {
        const response = await fetch(`${API_BASE_URL}/dashboard/stats`, {
            headers: getAuthHeaders()
        });
        return response.json();
    }
};

// Make API available globally
window.api = api;


