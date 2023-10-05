
from main import db

class Roster(db.Model):
    __tablename__ = "rosters"

    id = db.Column(db.Integer, primary_key = True)
    roster_slot = db.Column(db.String(50), nullable = False)

    # Define Foreign Keys
    player_id = db.Column(db.Integer, db.ForeignKey("players.id"))
    team_id = db.Column(db.Integer, db.ForeignKey("teams.id"), nullable = False)

    # Define relationships
    team = db.relationship("Team", back_populates="roster")
    player = db.relationship("Player", back_populates="rosters")
    
