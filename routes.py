from flask import render_template, request, redirect, session, url_for, flash
from app import app, db
from models import User, SkincareStep, WellnessActivity, Goal, DailyCheckin
from datetime import date
from textblob import TextBlob
from app import db, Mood
from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash
@app.route('/toggle_goal_completion/<int:goal_id>', methods=['POST'])
def toggle_goal_completion(goal_id):
    if 'user_id' not in session:
        flash("Please log in to manage your goals.", 'error')
        return redirect(url_for('login'))

    goal_to_toggle = Goal.query.get(goal_id)
    if not goal_to_toggle:
        flash("Goal not found.", 'error')
        return redirect(url_for('dashboard'))

    # Security check: Ensure the current user owns this goal
    if goal_to_toggle.user_id != session['user_id']:
        flash("You are not authorized to modify this goal.", 'error')
        return redirect(url_for('dashboard'))

    try:
        goal_to_toggle.completed = not goal_to_toggle.completed # Toggle the completion status
        db.session.commit()
        if goal_to_toggle.completed:
            flash("Goal marked as completed!", 'success')
        else:
            flash("Goal marked as ongoing.", 'info') # If they un-mark it
    except Exception as e:
        db.session.rollback()
        flash(f"Error updating goal status: {e}", 'error')
    return redirect(url_for('dashboard'))
# --- Splash Route ---
@app.route('/')
def home():
    # It's generally good practice to check if a user is already logged in
    # and redirect them to their dashboard if they are.
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return render_template('splash.html')

# --- Signup Route ---
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if 'user_id' in session: # If already logged in, redirect to dashboard
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = generate_password_hash(request.form['password'], method='pbkdf2:sha256')
        skin_type = request.form['skin_type']

        if User.query.filter_by(email=email).first():
            flash("Email already exists!", 'error') # Added 'error' category
            return redirect(url_for('signup'))

        try:
            user = User(name=name, email=email, password=password, skin_type=skin_type)
            db.session.add(user)
            db.session.commit()
            session['user_id'] = user.id
            flash("Account created successfully! Welcome to GlowMe!", 'success') # Added 'success' category
            return redirect(url_for('dashboard'))
        except Exception as e:
            db.session.rollback()
            flash(f"An error occurred during signup: {e}", 'error') # Added error handling
            return redirect(url_for('signup'))

    return render_template('signup.html')

# --- Login Route ---
@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_id' in session: # If already logged in, redirect to dashboard
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            flash("Logged in successfully!", 'success') # Added 'success' category
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid email or password.", 'error') # Added 'error' category
            return redirect(url_for('login'))

    return render_template('login.html')

# --- Logout Route ---
@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out.", 'info') # Changed to 'info' category for logout
    return redirect(url_for('home'))

# --- Dashboard Route ---
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash("Please log in to view your dashboard.", 'error') # Added flash message for unauthorized access
        return redirect(url_for('login'))

    user = User.query.get(session['user_id'])
    if not user: # Handle case where user_id in session doesn't exist in DB (e.g., deleted user)
        session.clear()
        flash("Your session is invalid. Please log in again.", 'error')
        return redirect(url_for('login'))

    checkin = DailyCheckin.query.filter_by(user_id=user.id, date=date.today()).first()
    # Ordered by creation date descending to show newest first
    steps = SkincareStep.query.filter_by(user_id=user.id).order_by(SkincareStep.id.desc()).all()
    activities = WellnessActivity.query.filter_by(user_id=user.id).order_by(WellnessActivity.id.desc()).all()
    goals = Goal.query.filter_by(user_id=user.id).order_by(Goal.id.desc()).all()

    return render_template('dashboard.html', user=user, checkin=checkin, steps=steps, activities=activities, goals=goals)

# --- Daily Check-in ---
@app.route('/daily_checkin', methods=['POST'])
def daily_checkin():
    if 'user_id' not in session:
        flash("Please log in to add a check-in.", 'error')
        return redirect(url_for('login'))

    mood = request.form['mood']
    energy = request.form['energy']

    try:
        checkin = DailyCheckin(user_id=session['user_id'], mood=mood, energy=energy, date=date.today())
        db.session.add(checkin)
        db.session.commit()
        flash("Daily check-in saved successfully!", 'success')
    except Exception as e:
        db.session.rollback()
        flash(f"Error saving check-in: {e}", 'error')
    return redirect(url_for('dashboard'))

# --- Add Skincare Step ---
@app.route('/add_skincare_step', methods=['POST'])
def add_skincare_step():
    if 'user_id' not in session:
        flash("Please log in to add skincare steps.", 'error')
        return redirect(url_for('login'))

    routine_type = request.form['routine_type']
    step_name = request.form['step_name']
    product_name = request.form['product_name']

    try:
        step = SkincareStep(user_id=session['user_id'], routine_type=routine_type, step_name=step_name, product_name=product_name)
        db.session.add(step)
        db.session.commit()
        flash("Skincare step added successfully!", 'success')
    except Exception as e:
        db.session.rollback()
        flash(f"Error adding skincare step: {e}", 'error')
    return redirect(url_for('dashboard'))

# --- Add Activity ---
@app.route('/add_activity', methods=['POST'])
def add_activity():
    if 'user_id' not in session:
        flash("Please log in to add activities.", 'error')
        return redirect(url_for('login'))

    activity_type = request.form['activity_type']
    duration = request.form['duration']
    notes = request.form.get('notes')

    try:
        activity = WellnessActivity(user_id=session['user_id'], activity_type=activity_type, duration=duration, notes=notes)
        db.session.add(activity)
        db.session.commit()
        flash("Wellness activity logged successfully!", 'success')
    except Exception as e:
        db.session.rollback()
        flash(f"Error logging activity: {e}", 'error')
    return redirect(url_for('dashboard'))

# --- Add Goal ---
@app.route('/add_goal', methods=['POST'])
def add_goal():
    if 'user_id' not in session:
        flash("Please log in to add goals.", 'error')
        return redirect(url_for('login'))

    title = request.form['title']
    description = request.form['description']

    try:
        goal = Goal(user_id=session['user_id'], title=title, description=description)
        db.session.add(goal)
        db.session.commit()
        flash("Goal added successfully!", 'success')
    except Exception as e:
        db.session.rollback()
        flash(f"Error adding goal: {e}", 'error')
    return redirect(url_for('dashboard'))

# --- Delete Skincare Step ---
@app.route('/delete_skincare_step/<int:step_id>', methods=['POST'])
def delete_skincare_step(step_id):
    if 'user_id' not in session:
        flash("Please log in to delete skincare steps.", 'error')
        return redirect(url_for('login'))

    step_to_delete = SkincareStep.query.get(step_id) # Use .get() for primary key lookup
    if not step_to_delete: # Check if step exists
        flash("Skincare step not found.", 'error')
        return redirect(url_for('dashboard'))

    # Security check: Ensure the current user owns this step
    if step_to_delete.user_id != session['user_id']:
        flash("You are not authorized to delete this skincare step.", 'error')
        return redirect(url_for('dashboard'))

    try:
        db.session.delete(step_to_delete)
        db.session.commit()
        flash("Skincare step deleted successfully!", 'success')
    except Exception as e:
        db.session.rollback()
        flash(f"Error deleting skincare step: {e}", 'error')
    return redirect(url_for('dashboard'))

# --- Delete Activity ---
@app.route('/delete_activity/<int:activity_id>', methods=['POST'])
def delete_activity(activity_id):
    if 'user_id' not in session:
        flash("Please log in to delete activities.", 'error')
        return redirect(url_for('login'))

    activity_to_delete = WellnessActivity.query.get(activity_id)
    if not activity_to_delete:
        flash("Wellness activity not found.", 'error')
        return redirect(url_for('dashboard'))

    if activity_to_delete.user_id != session['user_id']:
        flash("You are not authorized to delete this activity.", 'error')
        return redirect(url_for('dashboard'))

    try:
        db.session.delete(activity_to_delete)
        db.session.commit()
        flash("Wellness activity deleted successfully!", 'success')
    except Exception as e:
        db.session.rollback()
        flash(f"Error deleting activity: {e}", 'error')
    return redirect(url_for('dashboard'))

# --- Delete Goal ---
@app.route('/delete_goal/<int:goal_id>', methods=['POST'])
def delete_goal(goal_id):
    if 'user_id' not in session:
        flash("Please log in to delete goals.", 'error')
        return redirect(url_for('login'))

    goal_to_delete = Goal.query.get(goal_id)
    if not goal_to_delete:
        flash("Goal not found.", 'error')
        return redirect(url_for('dashboard'))

    if goal_to_delete.user_id != session['user_id']:
        flash("You are not authorized to delete this goal.", 'error')
        return redirect(url_for('dashboard'))

    try:
        db.session.delete(goal_to_delete)
        db.session.commit()
        flash("Goal deleted successfully!", 'success')
    except Exception as e:
        db.session.rollback()
        flash(f"Error deleting goal: {e}", 'error')
    return redirect(url_for('dashboard'))


# --- Product Suggestions ---
@app.route('/product_suggestions')
def product_suggestions():
    if 'user_id' not in session:
        flash("Please log in to view product suggestions.", 'error') # Added flash message
        return redirect(url_for('login'))

    user = User.query.get(session['user_id'])
    if not user:
        session.clear()
        flash("Your session is invalid. Please log in again.", 'error')
        return redirect(url_for('login'))

    skin_type = user.skin_type

    suggestions = {
        'dry': [
            {'name': 'Hydra Rich Cream', 'desc': 'Deep moisture for dry skin.', 'price': '$18', 'link': 'https://example.com/hydra-rich'},
            {'name': 'Aloe Soothing Gel', 'desc': 'Soothes and hydrates dry patches.', 'price': '$10', 'link': 'https://example.com/aloe-gel'}
        ],
        'oily': [
            {'name': 'Oil-Free Moisturizer', 'desc': 'Controls shine and hydrates.', 'price': '$16', 'link': 'https://example.com/oil-free'},
            {'name': 'Salicylic Acid Cleanser', 'desc': 'Great for acne-prone oily skin.', 'price': '$12', 'link': 'https://example.com/salicylic'}
        ],
        'combination': [
            {'name': 'Balanced Toner', 'desc': 'Balances oil and hydration.', 'price': '$14', 'link': 'https://example.com/toner'},
            {'name': 'Dual Action Cream', 'desc': 'Targets dry and oily zones.', 'price': '$20', 'link': 'https://example.com/dual-action'}
        ],
        'sensitive': [
            {'name': 'Cica Balm', 'desc': 'Reduces redness and irritation.', 'price': '$22', 'link': 'https://example.com/cica'},
            {'name': 'Gentle Cleanser', 'desc': 'Fragrance-free and calming.', 'price': '$15', 'link': 'https://example.com/gentle-cleanser'}
        ]
    }

    return render_template('products.html', suggestions=suggestions.get(skin_type.lower(), []), skin_type=skin_type)

# --- Skincare Tips Page ---
@app.route('/skincare_page')
def skincare_page():
    if 'user_id' not in session:
        flash("Please log in to view skincare tips.", 'error') # Added flash message
        return redirect(url_for('login'))

    user = User.query.get(session['user_id'])
    if not user:
        session.clear()
        flash("Your session is invalid. Please log in again.", 'error')
        return redirect(url_for('login'))

    skin_type = user.skin_type

    tips_dict = {
        'dry': [
            "Use thick moisturizers like shea butter or ceramides.",
            "Avoid hot water; opt for lukewarm.",
            "Use hydrating serums with hyaluronic acid."
        ],
        'oily': [
            "Use oil-free, non-comedogenic products.",
            "Cleanse twice daily with salicylic acid.",
            "Avoid over-exfoliating."
        ],
        'combination': [
            "Apply cream moisturizer to dry areas, gel to oily ones.",
            "Use a balancing toner with rose water.",
            "Stick to lightweight sunscreen."
        ],
        'sensitive': [
            "Avoid fragrances and alcohol in products.",
            "Use calming ingredients like oatmeal or Cica.",
            "Patch test every new product."
        ]
    }

    tips = tips_dict.get(skin_type.lower(), [])
    return render_template('skincare.html', skin_type=skin_type, tips=tips)

@app.route('/predict_mood', methods=['GET', 'POST'])
def predict_mood():
    mood = None
    if request.method == 'POST':
        text = request.form['journal_entry']
        analysis = TextBlob(text)
        polarity = analysis.sentiment.polarity

        if polarity > 0:
            mood = "😊 Positive"
        elif polarity < 0:
            mood = "😞 Negative"
        else:
            mood = "😐 Neutral"

        # Save mood to database
        new_mood = Mood(
            user_id=session['user_id'],
            entry=text,
            mood=mood,
            date=datetime.now().strftime("%Y-%m-%d")
        )
        db.session.add(new_mood)
        db.session.commit()

    return render_template('mood_predictor.html', mood=mood)

@app.route('/mood_history')
def mood_history():
    if 'user_id' not in session:
        return redirect('/login')  # User must be logged in
    moods = Mood.query.filter_by(user_id=session['user_id']).order_by(Mood.date.desc()).all()
    return render_template('mood_history.html', moods=moods)
