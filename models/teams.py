# from main import db

# class Team(db.Model):
#     __tablename__ = "teams"

#     id = db.Column(db.Integer, primary_key = True)

#     team_name = db.Column(db.Text, nullable = False)
#     #roster = db.Col


#     user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
#     league_id = db.Column(db.Integer, db.ForeignKey("leagues.id"), nullable=False)
#     # points_scored = db.Column(db.Integer, db.ForienKey(ullable = False) # amount of players allowed to be rostered on a team