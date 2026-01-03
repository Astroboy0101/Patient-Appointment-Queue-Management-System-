"""
Local Development Server
Serves frontend with localhost API URLs and starts backend server
"""

import http.server
import socketserver
import subprocess
import sys
import os
import time
import threading
import webbrowser
from pathlib import Path

PORT_FRONTEND = 8000
PORT_BACKEND = 5000

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom handler that injects local API URLs into HTML files"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory='frontend', **kwargs)
    
    def end_headers(self):
        # Add CORS headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        super().end_headers()
    
    def do_GET(self):
        # Handle root path
        if self.path == '/' or self.path == '':
            self.path = '/index.html'
        
        # Check if it's an HTML file
        if self.path.endswith('.html'):
            file_path = Path('frontend') / self.path.lstrip('/')
            if file_path.exists():
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                # Read and modify HTML to use local API
                content = file_path.read_text(encoding='utf-8')
                # Replace API URLs
                content = content.replace('js/api.js', 'js/api_local.js')
                content = content.replace('js/auth.js', 'js/auth_local.js')
                # Fix navigation links to be absolute
                content = content.replace('href="login.html"', 'href="/login.html"')
                content = content.replace('href="signup.html"', 'href="/signup.html"')
                content = content.replace('href="dashboard.html"', 'href="/dashboard.html"')
                content = content.replace('href="about.html"', 'href="/about.html"')
                content = content.replace('href="patient-registration.html"', 'href="/patient-registration.html"')
                content = content.replace('href="appointment.html"', 'href="/appointment.html"')
                content = content.replace('href="search.html"', 'href="/search.html"')
                content = content.replace('href="admin.html"', 'href="/admin.html"')
                content = content.replace('href="forgot-password.html"', 'href="/forgot-password.html"')
                content = content.replace('href="index.html"', 'href="/index.html"')
                
                self.wfile.write(content.encode('utf-8'))
                return
        
        # Serve other files normally (CSS, JS, images, etc.)
        return super().do_GET()

def start_backend():
    """Start Flask backend server"""
    project_root = Path(__file__).parent
    backend_dir = project_root / 'backend'
    os.chdir(backend_dir)
    
    try:
        # Activate venv and run Flask
        if sys.platform == 'win32':
            python_exe = backend_dir / 'venv' / 'Scripts' / 'python.exe'
        else:
            python_exe = backend_dir / 'venv' / 'bin' / 'python'
        
        subprocess.run([str(python_exe), 'app.py'], check=True)
    except KeyboardInterrupt:
        print("\n[Backend] Server stopped")
    except Exception as e:
        print(f"\n[Backend] Error: {e}")

def start_frontend():
    """Start frontend HTTP server"""
    # Make sure we're in the project root
    project_root = Path(__file__).parent
    os.chdir(project_root)
    
    handler = CustomHTTPRequestHandler
    
    with socketserver.TCPServer(("", PORT_FRONTEND), handler) as httpd:
        print(f"[Frontend] Server running at http://localhost:{PORT_FRONTEND}")
        print("[Frontend] Press Ctrl+C to stop")
        httpd.serve_forever()

def main():
    """Main function to start both servers"""
    print("=" * 50)
    print("Patient Queue System - Starting Servers")
    print("=" * 50)
    print()
    
    # Check if backend directory exists
    if not Path('backend').exists():
        print("[ERROR] Backend directory not found!")
        sys.exit(1)
    
    # Check if frontend directory exists
    if not Path('frontend').exists():
        print("[ERROR] Frontend directory not found!")
        sys.exit(1)
    
    # Start backend in separate thread
    print("[Backend] Starting Flask server...")
    backend_thread = threading.Thread(target=start_backend, daemon=True)
    backend_thread.start()
    
    # Wait for backend to start
    print("[Backend] Waiting for server to start...")
    time.sleep(5)
    
    # Test backend
    try:
        import urllib.request
        response = urllib.request.urlopen(f'http://localhost:{PORT_BACKEND}/api/health', timeout=3)
        if response.status == 200:
            print("[Backend] Server is running!")
        else:
            print("[WARNING] Backend may still be starting...")
    except:
        print("[WARNING] Backend may still be starting...")
    
    print()
    print("[Frontend] Starting HTTP server...")
    
    # Open browser after a short delay
    def open_browser():
        time.sleep(2)
        webbrowser.open(f'http://localhost:{PORT_FRONTEND}/index.html')
    
    browser_thread = threading.Thread(target=open_browser, daemon=True)
    browser_thread.start()
    
    # Start frontend server (this blocks)
    try:
        start_frontend()
    except KeyboardInterrupt:
        print("\n[Frontend] Server stopped")
        print("[Backend] Server stopped")
        sys.exit(0)

if __name__ == '__main__':
    main()

