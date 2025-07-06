from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///glowme.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# ------------------------------
# Define Mood model (for mood predictor)
# ------------------------------
class Mood(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    entry = db.Column(db.Text, nullable=False)
    mood = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(20), nullable=False)

# ------------------------------
# Import routes after db/models
# ------------------------------
from routes import *

# ------------------------------
# Create DB tables automatically
# ------------------------------
with app.app_context():
    db.create_all()

# ------------------------------
# Run Flask app
# ------------------------------
if __name__ == '__main__':
    app.run(debug=True)
