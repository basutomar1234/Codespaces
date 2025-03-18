import os
import subprocess
import datetime
from django.http import HttpResponse
import pytz
import getpass

def htop_view(request):
    # Get system username safely
    username = "codespace"  # Alternative to os.getlogin()

    # Get current IST time
    ist = pytz.timezone('Asia/Kolkata')
    current_time = datetime.datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')

    # Get top output
    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')
    except Exception as e:
        top_output = str(e)

    response_content = f"""
    <html>
    <body>
        <h1>System Information</h1>
        <p><strong>Name:</strong> Vipasha Tomar </p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time (IST):</strong> {current_time}</p>
        <h2>Top Output:</h2>
        <pre>{top_output}</pre>
    </body>
    </html>
    """
    return HttpResponse(response_content)
