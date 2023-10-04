# Roster (to represent the players on a team)
# - id
# - team_id (FK to Team)
# - player_id (FK to Player)
# - position (e.g., QB, RB, WR, etc.)

# from main import db

# class Roster(db.Model):
#     __tablename__ = "teams"

#     id = db.Column(db.Integer, primary_key = True)

#     position = db.Column(db.String, nullabe = False)
#     position_counter = db.Column(db.Integer, nullable = False)
# #     #starters = db.Column(db.Test) # potentialy a foreign key
# #     #bench = db.Column(db.Test) # potentialy a foreign key

#     player_id = db.Column(db.Integer, db.ForeignKey("players.id"))
#     team_id = db.Colimn(db.Integer, db.ForeignKey("teams.id"), nullable = False)

#     leagues = db.relationship("League", back_populates="teams", cascade="all, delete")
#     user = db.relationship("User", back_populates="teams")

#     # points_scored = db.Column(db.Integer, db.ForienKey(ullable = False) # amount of players allowed to be rostered on a team