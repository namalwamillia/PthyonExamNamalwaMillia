from app.extensions import db
from datetime import datetime

class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    contact = db.Column(db.String(50), nullable=False, unique=True)
  

    def __init__(self, first_name, last_name, email, contact ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.contact = contact
      

    def get_full_name(self):
        return f"{self.last_name} {self.first_name}"
        
        