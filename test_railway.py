"""
Test script for Railway deployment
Tests all endpoints and functionality
"""

import requests
import json
import sys

RAILWAY_URL = "https://web-production-d92ae.up.railway.app"
BASE_URL = f"{RAILWAY_URL}/api"

def test_health():
    """Test health endpoint"""
    print("\n[TEST] Health Check...")
    try:
        response = requests.get(f"{BASE_URL}/health", timeout=15)
        if response.status_code == 200:
            data = response.json()
            print(f"  [OK] Status: {response.status_code}")
            print(f"  [OK] Message: {data.get('message')}")
            return True
        else:
            print(f"  [ERROR] Status: {response.status_code}")
            return False
    except Exception as e:
        print(f"  [ERROR] {str(e)}")
        return False

def test_doctors():
    """Test doctors endpoint"""
    print("\n[TEST] Doctors API...")
    try:
        response = requests.get(f"{BASE_URL}/doctors", timeout=15)
        if response.status_code == 200:
            data = response.json()
            doctors = data.get('doctors', [])
            print(f"  [OK] Status: {response.status_code}")
            print(f"  [OK] Doctors found: {len(doctors)}")
            for doctor in doctors[:3]:  # Show first 3
                print(f"    - {doctor.get('name')} ({doctor.get('id')})")
            return True
        else:
            print(f"  [ERROR] Status: {response.status_code}")
            return False
    except Exception as e:
        print(f"  [ERROR] {str(e)}")
        return False

def test_authentication():
    """Test authentication endpoints"""
    print("\n[TEST] Authentication...")
    
    # Test signup
    print("  Testing signup...")
    try:
        signup_data = {
            "email": f"test_{hash('test')}@test.com",
            "password": "test123",
            "name": "Test User"
        }
        response = requests.post(f"{BASE_URL}/auth/signup", 
                               json=signup_data, timeout=15)
        if response.status_code == 201:
            data = response.json()
            token = data.get('token')
            print(f"    [OK] Signup successful, token received")
            return token
        else:
            print(f"    [WARNING] Signup: {response.status_code}")
            print(f"    Response: {response.text}")
    except Exception as e:
        print(f"    [ERROR] Signup failed: {str(e)}")
    
    return None

def test_protected_routes(token):
    """Test protected routes"""
    print("\n[TEST] Protected Routes...")
    
    headers = {}
    if token:
        headers['Authorization'] = f'Bearer {token}'
    
    # Test patients endpoint
    print("  Testing patients endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/patients", 
                              headers=headers, timeout=15)
        if response.status_code == 200:
            data = response.json()
            patients = data.get('patients', [])
            print(f"    [OK] Patients endpoint: {response.status_code}")
            print(f"    [OK] Patients found: {len(patients)}")
            return True
        elif response.status_code == 401:
            print(f"    [OK] Correctly requires authentication (401)")
            return True
        else:
            print(f"    [WARNING] Status: {response.status_code}")
            return False
    except Exception as e:
        print(f"    [ERROR] {str(e)}")
        return False

def test_queue(token):
    """Test queue endpoints"""
    print("\n[TEST] Queue Management...")
    
    headers = {}
    if token:
        headers['Authorization'] = f'Bearer {token}'
    
    try:
        response = requests.get(f"{BASE_URL}/queue", 
                              headers=headers, timeout=15)
        if response.status_code == 200:
            data = response.json()
            print(f"    [OK] Queue endpoint: {response.status_code}")
            print(f"    [OK] Regular queue size: {data.get('regular_size', 0)}")
            print(f"    [OK] Emergency queue size: {data.get('emergency_size', 0)}")
            return True
        elif response.status_code == 401:
            print(f"    [OK] Correctly requires authentication (401)")
            return True
        else:
            print(f"    [WARNING] Status: {response.status_code}")
            return False
    except Exception as e:
        print(f"    [ERROR] {str(e)}")
        return False

def main():
    """Run all tests"""
    print("=" * 60)
    print("RAILWAY DEPLOYMENT TEST SUITE")
    print("=" * 60)
    print(f"\nTesting: {RAILWAY_URL}")
    
    results = {
        'health': False,
        'doctors': False,
        'auth': False,
        'protected': False,
        'queue': False
    }
    
    # Run tests
    results['health'] = test_health()
    results['doctors'] = test_doctors()
    token = test_authentication()
    results['auth'] = token is not None
    results['protected'] = test_protected_routes(token)
    results['queue'] = test_queue(token)
    
    # Summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    for test, passed in results.items():
        status = "[OK]" if passed else "[FAIL]"
        print(f"{status} {test.upper()}")
    
    all_passed = all(results.values())
    print("\n" + "=" * 60)
    if all_passed:
        print("ALL TESTS PASSED!")
    else:
        print("SOME TESTS FAILED - Review errors above")
    print("=" * 60)
    
    return 0 if all_passed else 1

if __name__ == '__main__':
    sys.exit(main())

