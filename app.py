from flask import Flask, request, redirect
from datetime import datetime

app = Flask(__name__)

# Log file to store IP and User-Agent data
LOG_FILE = 'logs.txt'
REDIRECT_URL = 'https://yourdomain.com/final_image.jpg'  # Replace with your actual image URL

@app.route('/')
def log_ip():
    # Get user info
    ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Log IP and User-Agent in a text file
    with open(LOG_FILE, 'a') as f:
        f.write(f"[{timestamp}] IP: {ip} | UA: {user_agent}\n")

    # Redirect to the final image URL
    return redirect(REDIRECT_URL)

if __name__ == '__main__':
    app.run(debug=True)
