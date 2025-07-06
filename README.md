GlowMe: Your Personal Skincare & Wellness Companion 🌿✨

Overview
GlowMe is a web-based application designed to be your all-in-one personal assistant for skincare and overall well-being. It helps you track your daily routines, monitor your mood and energy, log various wellness activities, set personal goals, and receive smart, personalized recommendations. Built with Python's Flask framework, a lightweight database (SQLite), and integrated AI/ML features, GlowMe aims to make your journey towards holistic health easy and insightful.

Features
GlowMe offers a rich set of functionalities to support your wellness journey:

Core System Features:
User Account Management: Secure sign-up, login, and logout.

Personalized Dashboard: A central hub displaying your health overview.

Dynamic Notifications: Quick messages for success, errors, and information.

Data Persistence: All your data (users, routines, activities, goals) is safely stored in a database.

Responsive Design: Works well and looks great on any device (desktop, tablet, mobile).

Easy Navigation: Clear links and a streamlined interface for smooth app usage.

Daily Tracking & Wellness:
Daily Wellness Check-in: Log your mood and energy levels every day.

Comprehensive Activity Logging: Record various wellness activities (e.g., Yoga, Meditation, Reading) with duration and notes.

Activity History: View a chronological list of all your logged activities.

Activity Management: Option to remove or edit past activities.

Skincare Routine & AI Recommendations:
Customizable AM/PM Routines: Manually add, view, and organize your morning and evening skincare steps (step name, product name).

Skincare Step Management: Remove individual steps from your routines.

AI-Driven Skincare Recommendations: Get smart suggestions for morning and evening skincare steps based on your skin type.

Automated Routine Integration: Quickly add AI-suggested steps to your routine with one click.

Goal Management:
Personal Goal Setting: Define new personal health goals with a title and optional target date.

Goal Tracking: View a list of all active and completed goals.

Goal Status Updates: Mark goals as completed.

Goal Removal: Option to remove goals from your list.

Information & Insights:
Informational Skincare Guidance: Access general skincare tips and advice within the app.

Personalized Product Recommendations (AI/ML): Receive a specific list of skincare product ideas tailored to your skin type.

Mood Prediction from User Text (AI/ML): The system analyzes your written input to classify your current mood.

Technologies Used
Backend: Python 3.x, Flask (Web Framework)

Database: SQLite, Flask-SQLAlchemy (ORM)

Frontend: HTML5, CSS3 (Custom & Responsive), Vanilla JavaScript

AI/ML: Rule-Based Systems (for recommendations and mood classification)

Icons: Font Awesome

Development Environment: Visual Studio Code

Setup and Installation
Follow these steps to get GlowMe running on your local machine:

Clone the Repository:

git clone https://github.com/your-username/GlowMe.git
cd GlowMe

(Replace your-username with your GitHub username.)

Create and Activate a Virtual Environment:

python -m venv venv
.\venv\Scripts\activate   # For Windows

Install Dependencies:

pip install -r requirements.txt

Download TextBlob Corpora (for AI/ML):

python -m textblob.download_corpora

Run the Flask Application:

set FLASK_APP=app.py
set FLASK_DEBUG=1
python -m flask run

Usage
Once the Flask application is running, open your web browser and go to:
http://127.0.0.1:5000/signup

Sign Up: Create a new account with your details and skin type.

Log In: Use your new credentials to access your personalized dashboard.

Explore: Start logging your daily mood, adding skincare steps, setting wellness goals, and tracking your activities!

AI/ML Integration Details
GlowMe incorporates two key AI/ML functionalities:

Mood Prediction from User Text: When you input text (e.g., in a daily check-in or future journaling feature), the system processes this text to classify your current mood. This helps in understanding your emotional state.

Skin Type-Based Product Recommendations: Based on the skin type you provide during registration, GlowMe suggests suitable skincare product categories and their general descriptions. This is a rule-based system designed to give you relevant initial guidance.

Future Enhancements
We plan to expand GlowMe's capabilities with features such as:

Advanced progress visualization (charts & graphs).

Customizable reminders for routines and goals.

Community features for sharing and challenges.

A dedicated journaling module.

Basic nutrition tracking.

More advanced AI, including predictive analytics for mood trends and image-based skin analysis.

Browser push notifications.

Multi-language support.

Integration with a larger product database.


License
This project is open-source and available under the MIT License. (You can create a LICENSE file in your repository with the MIT License text if you choose this.)
