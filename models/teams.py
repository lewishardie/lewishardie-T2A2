from main import db

class Team(db.Model):
    __tablename__ = "teams"

    id = db.Column(db.Integer, primary_key = True)

    team_name = db.Column(db.String, nullable = False)
#     #starters = db.Column(db.Test) # potentialy a foreign key
#     #bench = db.Column(db.Test) # potentialy a foreign key


    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    league_id = db.Column(db.Integer, db.ForeignKey("leagues.id"), nullable=False)

    leagues = db.relationship("League", back_populates="teams", cascade="all, delete")
    user = db.relationship("User", back_populates="teams")

#     # points_scored = db.Column(db.Integer, db.ForienKey(ullable = False) # amount of players allowed to be rostered on a team