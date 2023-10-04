from main import db

class User(db.Model):
    __tablename__ = "users"
    # primary key
    id = db.Column(db.Integer, primary_key = True)
    # rest of the attributes
    username = db.Column(db.String(25), unique = True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique = True)
    password = db.Column(db.String(100))
    # admin = db.Column(db.Boolean, default = False)

    # relationships
    leagues = db.relationship("League", back_populates="users")
    teams = db.relationship("Team", back_populates="user")

    admin_league = db.relationship('League', back_populates="admin")

    # league = db.relationship('League', back_populates="team")
    # teams = db.relationship('Team', back_populates="user")
