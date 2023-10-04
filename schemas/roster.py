# from main import ma
# from marshmallow import fields

# class RosterSchema(ma.Schema):

#     class Meta:
#         fields = (
#             "id",
#             "team_id",
#             "player_id",
#             "positions", 
#             "position_counter",
#             # "user",
#             # "league",
#         )

#     user = fields.Nested("UserSchema", only=("username",), exclude=("leagues", "admin_league", ))
#     league = fields.Nested("LeagueSchema", only=("league_name",))

# roster_schema = RosterSchema()
# rosters_schema = RosterSchema(many = True)