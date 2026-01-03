/**
 * Authentication Utilities
 * Handles login, signup, logout, and session management
 */

const API_BASE_URL = 'http://localhost:5000/api';

// Get token from localStorage or session
function getToken() {
    return localStorage.getItem('token') || sessionStorage.getItem('token');
}

// Save token
function saveToken(token, remember = false) {
    if (remember) {
        localStorage.setItem('token', token);
    } else {
        sessionStorage.setItem('token', token);
    }
}

// Remove token
function removeToken() {
    localStorage.removeItem('token');
    sessionStorage.removeItem('token');
}

// Check if user is authenticated
function isAuthenticated() {
    return !!getToken();
}

// Get current user
async function getCurrentUser() {
    const token = getToken();
    if (!token) return null;

    try {
        const response = await fetch(`${API_BASE_URL}/auth/me`, {
            headers: {
                'Authorization': `Bearer ${token}`
            }
        });

        if (response.ok) {
            const data = await response.json();
            return data.user;
        }
    } catch (error) {
        console.error('Error getting current user:', error);
    }
    return null;
}

// Login
async function login(email, password) {
    try {
        const response = await fetch(`${API_BASE_URL}/auth/login`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email, password })
        });

        const data = await response.json();

        if (response.ok) {
            saveToken(data.token, true);
            return { success: true, user: data.user };
        } else {
            return { success: false, error: data.error || 'Login failed' };
        }
    } catch (error) {
        return { success: false, error: 'Network error. Please try again.' };
    }
}

// Signup
async function signup(name, email, password) {
    try {
        const response = await fetch(`${API_BASE_URL}/auth/signup`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ name, email, password })
        });

        const data = await response.json();

        if (response.ok) {
            saveToken(data.token, true);
            return { success: true, user: data.user };
        } else {
            return { success: false, error: data.error || 'Signup failed' };
        }
    } catch (error) {
        return { success: false, error: 'Network error. Please try again.' };
    }
}

// Logout
async function logout() {
    const token = getToken();
    if (token) {
        try {
            await fetch(`${API_BASE_URL}/auth/logout`, {
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${token}`
                }
            });
        } catch (error) {
            console.error('Logout error:', error);
        }
    }
    removeToken();
    window.location.href = '/index.html';
}

// Forgot password
async function forgotPassword(email) {
    try {
        const response = await fetch(`${API_BASE_URL}/auth/forgot-password`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email })
        });

        const data = await response.json();

        if (response.ok) {
            return { success: true, verification_code: data.verification_code };
        } else {
            return { success: false, error: data.error || 'Failed to send verification code' };
        }
    } catch (error) {
        return { success: false, error: 'Network error. Please try again.' };
    }
}

// Reset password
async function resetPassword(email, code, newPassword) {
    try {
        const response = await fetch(`${API_BASE_URL}/auth/reset-password`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email, code, new_password: newPassword })
        });

        const data = await response.json();

        if (response.ok) {
            return { success: true };
        } else {
            return { success: false, error: data.error || 'Password reset failed' };
        }
    } catch (error) {
        return { success: false, error: 'Network error. Please try again.' };
    }
}

// Check admin access
async function checkAdminAccess() {
    const token = getToken();
    if (!token) return false;

    try {
        const response = await fetch(`${API_BASE_URL}/admin/access`, {
            headers: {
                'Authorization': `Bearer ${token}`
            }
        });

        if (response.ok) {
            const data = await response.json();
            return data.has_access;
        }
    } catch (error) {
        console.error('Error checking admin access:', error);
    }
    return false;
}

// Require authentication (redirect if not logged in)
function requireAuth() {
    if (!isAuthenticated()) {
        const currentPage = window.location.pathname;
        if (!currentPage.includes('index.html') && !currentPage.includes('login.html') && !currentPage.includes('signup.html')) {
            window.location.href = '/login.html?redirect=' + encodeURIComponent(currentPage);
        }
    }
}

// Make auth functions available globally
window.auth = {
    getToken,
    saveToken,
    removeToken,
    isAuthenticated,
    getCurrentUser,
    login,
    signup,
    logout,
    forgotPassword,
    resetPassword,
    checkAdminAccess,
    requireAuth
};


