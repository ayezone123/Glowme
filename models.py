from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))
    skin_type = db.Column(db.String(50))

class SkincareStep(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    routine_type = db.Column(db.String(50))
    step_name = db.Column(db.String(100))
    product_name = db.Column(db.String(100))

class WellnessActivity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    activity_type = db.Column(db.String(100))
    duration = db.Column(db.Integer)
    notes = db.Column(db.Text)

class Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    completed = db.Column(db.Boolean, default=False)

class DailyCheckin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    mood = db.Column(db.String(100))
    energy = db.Column(db.String(100))
    date = db.Column(db.Date)
