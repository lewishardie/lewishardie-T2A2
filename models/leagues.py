# from main import db

# class League(db.Model):
#     __tablename__ = "leagues"

#     id = db.Column(db.Integer, primary_key = True)

#     name = db.Column(db.Text, nullable = False)
#     description = db.Column(db.Text)
#     start_date = db.Column(db.DateTime)
#     end_date = db.Column(db.DateTime)
#     max_players_per_team = db.Column(db.Integer, nullable = False, default = 15) # amount of players allowed to be rostered on a team
#     max_teams = db.Column(db.Integer, nullable = False, default = 12) # preferably even teams
#     max_bench = db.Column(db.Integer, nullable = False, default = 6) # players 
#     roster_positions = db.Column(db.Text) # maybe break this off elsewhere
#     commissioner = db.Column(db.Boolean, nullable = False, default = False) # owner of the league