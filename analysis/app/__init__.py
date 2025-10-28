from flask import Flask
app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this-in-production'  # For session management
from app import routes
