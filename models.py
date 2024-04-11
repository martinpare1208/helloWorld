from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = "student"

    student_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.VARCHAR(100), nullable=True)
    major_id = db.Column(db.Integer, db.ForeignKey('major.major_id'))
    birth_date = db.Column(db.DateTime, nullable=False)
    num_credits_completed = db.Column(db.Integer, nullable=False)
    gpa = db.Column(db.Float, nullable=False)
    is_honors = db.Column(db.Boolean, nullable=False)

    def __init__(self, first_name, last_name, email, major_id, birth_date, is_honors):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.major_id = major_id
        self.birth_date = birth_date
        self.num_credits_completed = 0
        self.gpa = 0.0
        self.is_honors = is_honors

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"

class Major(db.Model):
    __tablename__ = "major"

    major_id = db.Column(db.Integer, primary_key=True)
    major = db.Column(db.String(30), nullable=False)
    students = db.relationship('Student', backref='students')

    def __init__(self, major):
        self.major = major

    def __repr__(self):
        return f"{self.major}"

#Created a table to store user accounts
class User(UserMixin, db.Model):
    __tablename__ = "user"

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.VARCHAR(20), unique=True, nullable=False)
    password = db.Column(db.VARCHAR(30), nullable=False)
    role = db.Column(db.String(30), nullable=False)

#Constructor for user objects
    def __init__(self, user_id, username, password, role):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.role = role

    #function for Flask to know which user is logged in
    def get_id(self):
        return self.user_id
    def __repr__(self):
        return f"{self.username}"

