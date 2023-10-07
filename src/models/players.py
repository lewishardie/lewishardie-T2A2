# Import the 'db' instance from the 'main' module
from main import db
# Define the 'Player' model
class Player(db.Model):
    __tablename__ = "players"
    # Primary Key
    id = db.Column(db.Integer, primary_key = True)
    # Define attributes
    first_name = db.Column(db.String(50), nullable = False)
    last_name = db.Column(db.String(50), nullable = False)
    position = db.Column(db.String(50), nullable = False)
    nfl_team = db.Column(db.String(50), nullable = False)
    is_available = db.Column(db.Boolean, default=True)

    # Define Foreign Keys
    league_id = db.Column(db.Integer, db.ForeignKey("leagues.id"))

    # Define Relationships
    rosters = db.relationship("Roster", back_populates="player")
    
    # leagues = db.relationship("League", back_populates="players")