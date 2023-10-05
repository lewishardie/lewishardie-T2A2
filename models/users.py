from main import db

class User(db.Model):
    __tablename__ = "users"


    id = db.Column(db.Integer, primary_key = True)

    username = db.Column(db.String(25), unique = True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique = True)
    password = db.Column(db.String(100))

    # Define relationships
    leagues = db.relationship("League", back_populates="users", cascade="all, delete")
    teams = db.relationship("Team", back_populates="user", cascade="all, delete")
