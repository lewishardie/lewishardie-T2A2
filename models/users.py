from main import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    
    username = db.Column(db.Text, nullable = False, unique = True)
    first_name = db.Column(db.Text, nullable = False)
    last_name = db.Column(db.Text, nullable = False)
    email = db.Column(db.Text, nullable = False, unique = True)
    password = db.Column(db.Text, nullable = False)
