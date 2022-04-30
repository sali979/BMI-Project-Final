from flask_login import UserMixin
from __init__ import db
from services.age_calculator import calculate_age
from services.bmi_calculator import bmi_evaluation, bmi_score
from services.recommendation import give_recommendation


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    password = db.Column(db.String(100))
    username = db.Column(db.String(1000))

    def __init__(self, username: str):
        self.username = username


class Record(db.Model):
    __tablename__ = 'records'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    gender = db.Column(db.String(1))
    height = db.Column(db.Float)
    weight = db.Column(db.Float)
    age = db.Column(db.Integer)
    evaluation = db.Column(db.String(200))
    score = db.Column(db.Float)
    recommendation = db.Column(db.String(200))
    target = db.Column(db.Float)

    # Create relationship between user and records
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user_record = db.relationship(User, backref=db.backref('records', lazy=True))

    def __init__(self, height: float, weight: float, user_id: int, gender, date_of_birth: str, target: float):
        self.height = height
        self.weight = weight
        self.user_id = user_id
        self.gender = gender
        self.target = target
        self.age = calculate_age(date_of_birth)
        self.score = bmi_score(self.height, self.weight)
        self.evaluation = bmi_evaluation(self.height, self.weight)
        self.recommendation = give_recommendation(self.score, self.target)

    def to_string(self):
        return f"h: {self.height} inches and w: {self.weight} pounds"

    def __repr__(self):
        return f"<Record(id='{self.id}', user_id='{self.user_id}', gender='{self.gender}', age='{self.age}'," \
               f" height='{self.height}', weight='{self.weight}')> "
