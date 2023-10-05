from main import db

class Team(db.Model):
    __tablename__ = "teams"

    id = db.Column(db.Integer, primary_key = True)

    team_name = db.Column(db.String, nullable = False)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    league_id = db.Column(db.Integer, db.ForeignKey("leagues.id"), nullable=False)

    league = db.relationship("League", back_populates="teams", cascade="all, delete")
    user = db.relationship("User", back_populates="teams")
    roster = db.relationship("Roster", back_populates="team")

def create_roster(self):
        from models import Roster 
        roster = Roster(team_id=self.id)
        db.session.add(roster)
        db.session.commit()

def __init__(self, *args, **kwargs):
        super(Team, self).__init__(*args, **kwargs)
        self.create_roster()