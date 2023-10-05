from main import db

class League(db.Model):
    __tablename__ = "leagues"

    id = db.Column(db.Integer, primary_key = True)

    league_name = db.Column(db.Text, nullable = False)
    description = db.Column(db.Text)
    # start_date = db.Column(db.DateTime)
    # end_date = db.Column(db.DateTime)
    max_players_per_team = db.Column(db.Integer, nullable = False, default = 15) # amount of players allowed to be rostered on a team
    max_teams = db.Column(db.Integer, nullable = False, default = 12) # preferably even teams
    # max_bench = db.Column(db.Integer, nullable = False, default = 6) # players 
    # admin = db.Column(db.Boolean, default = False)

    admin_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    admin = db.relationship("User", foreign_keys=[admin_id])
    
    users = db.relationship("User", back_populates="leagues")
    
    teams = db.relationship("Team", back_populates="leagues")
    
                         
    # roster_positions = db.Column(db.Text) # maybe break this off elsewhere
    # commissioner = db.Column(db.Boolean, nullable = False, default = False) # owner of the league

    #user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)