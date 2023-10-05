from main import db

class League(db.Model):
    __tablename__ = "leagues"

    id = db.Column(db.Integer, primary_key = True)
    league_name = db.Column(db.Text, nullable = False)
    description = db.Column(db.Text)
    max_players_per_team = db.Column(db.Integer, nullable = False, default = 15) # amount of players allowed to be rostered on a team
    max_teams = db.Column(db.Integer, nullable = False, default = 12) # preferably even teams

    # Define Foreign Keys
    admin_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    
    # Define Relationships
    users = db.relationship("User", back_populates="leagues")
    teams = db.relationship("Team", back_populates="league", cascade="all, delete")
    
    # commissioner = db.relationship("User", foreign_keys=[admin_id])
    
                         
