"""
Script to update all HTML files to use absolute paths for Railway deployment
"""

from pathlib import Path
import re

FRONTEND_DIR = Path('frontend')

# Files to update
html_files = [
    'index.html',
    'login.html',
    'signup.html',
    'dashboard.html',
    'patient-registration.html',
    'appointment.html',
    'search.html',
    'admin.html',
    'forgot-password.html',
    'about.html'
]

def update_links(content):
    """Update relative links to absolute paths"""
    # Update href="filename.html" to href="/filename.html"
    content = re.sub(r'href="([^/][^"]*\.html)"', r'href="/\1"', content)
    # Update window.location.href = 'filename.html' to '/filename.html'
    content = re.sub(r"window\.location\.href\s*=\s*['\"]([^/][^'\"]*\.html)['\"]", r"window.location.href = '/\1'", content)
    # Update redirects
    content = re.sub(r"location\.href\s*=\s*['\"]([^/][^'\"]*\.html)['\"]", r"location.href = '/\1'", content)
    return content

for html_file in html_files:
    file_path = FRONTEND_DIR / html_file
    if file_path.exists():
        content = file_path.read_text(encoding='utf-8')
        updated = update_links(content)
        file_path.write_text(updated, encoding='utf-8')
        print(f"Updated: {html_file}")

print("\nAll HTML files updated for Railway deployment!")

