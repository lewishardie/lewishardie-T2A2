# Import the 'db' instance from the 'main' module
from main import db
# Define the 'Team' model
class Team(db.Model):
    __tablename__ = "teams"
    # Primary Key
    id = db.Column(db.Integer, primary_key = True)
    # Define attributes
    team_name = db.Column(db.String, nullable = False)
    # Define foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    league_id = db.Column(db.Integer, db.ForeignKey("leagues.id"), nullable=False)
    # Define relationships
    league = db.relationship("League", back_populates="teams", cascade="all, delete")
    user = db.relationship("User", back_populates="teams")
    roster = db.relationship("Roster", back_populates="team")

# Define a method to create a roster for the team
def create_roster(self):
        from models import Roster 
        roster = Roster(team_id=self.id)
        db.session.add(roster)
        db.session.commit()
# Constructor (__init__) method
def __init__(self, *args, **kwargs):
        super(Team, self).__init__(*args, **kwargs)
        self.create_roster()