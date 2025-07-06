GlowMe: Your Personal Skincare & Wellness Companion 🌿✨

Overview
GlowMe is a web-based application designed to be your all-in-one personal assistant for skincare and overall well-being. It helps you track your daily routines, monitor your mood and energy, log various wellness activities, set personal goals, and receive smart, personalized recommendations. Built with Python's Flask framework, a lightweight database (SQLite), and integrated AI/ML features, GlowMe's purpose is to make your journey towards holistic health easy and insightful.

Features
GlowMe offers many functionalities to support your wellness journey:

Core System Features:
User Account Management: Secure sign-up, login, and logout.

Personalized Dashboard: A central hub showing your health overview.

Dynamic Notifications: Fast messages for success, errors, and information.

Data Persistence: All your data (users, routines, activities, goals) is securely stored in the database.

Responsive Design: Works well and looks good on every device (desktop, tablet, mobile).

Easy Navigation: Clear links for easy movement between different sections of the app.

Daily Tracking & Wellness:
Daily Wellness Check-in: Log your mood and energy levels each day.

Comprehensive Activity Logging: Record various wellness activities (e.g., Yoga, Meditation, Reading) with duration and notes.

Activity History: View a chronological list of all your logged activities.

Activity Management: Option to remove or edit previously logged activities.

Skincare Routine & AI Recommendations:
Customizable AM/PM Routines: Manually add, view, and organize your morning and evening skincare steps (step name, product name).

Skincare Step Management: Remove individual steps from your routines.

AI-Driven Skincare Recommendations: Get smart suggestions for morning and evening skincare steps based on your skin type.

Automated Routine Integration: Add AI-suggested steps to your routine with one click.

Goal Management:
Personal Goal Setting: Define new personal health goals with a title and optional target date.

Goal Tracking: View a list of all active and completed goals.

Goal Status Updates: Mark goals as completed.

Goal Removal: Option to remove goals from the list.

Information & Insights:
Informational Skincare Guidance: Access general skincare tips and advice within the app.

Personalized Product Recommendations (AI/ML): Get a specific list of skincare product ideas tailored to your skin type.

Mood Prediction from User Text (AI/ML): The system analyzes your written text to classify your current mood.

Technologies Used
Backend: Python 3.11, Flask (Web Framework)

Database: SQLite, Flask-SQLAlchemy (ORM)

Frontend: HTML5, CSS3 (Custom & Responsive), Vanilla JavaScript

AI/ML: Rule-Based Systems (for recommendations and mood classification)

Icons: Font Awesome

Development Environment: Visual Studio Code

Setup and Installation
Follow these steps to run GlowMe on your local machine:

Clone the Repository:

git clone https://github.com/your-ayezone123/GlowMe.git
cd GlowMe

Create and Activate a Virtual Environment:

python -m venv venv
.\venv\Scripts\activate  

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
GlowMe includes two key AI/ML functionalities:

Mood Prediction from User Text: When you input text (e.g., in a daily check-in or future journaling feature), the system processes this text to classify your current mood. This helps in understanding your emotional state.

Skin Type-Based Product Recommendations: Based on the skin type you provide during registration, GlowMe suggests suitable skincare product categories and their general descriptions. This is a rule-based system designed to give you relevant initial guidance.

Future Enhancements
We plan to expand GlowMe's capabilities with these features:

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
This project is open-source and available under the MIT License.
