from main import ma
from marshmallow import fields

class LeagueSchema(ma.Schema):

    class Meta:
        fields = (
            "id", 
            "league_name", 
            "description", 
            "max_players_per_team", 
            "max_teams", 
            "max_bench", 
            "admin_id",
            "admin",
            "teams",
        )
        #load_only = ['teams']

    # users = fields.Nested("UserSchema", only=("username",))
    users = fields.Nested("UserSchema", only=("username",), exclude=("leagues", "admin_league", ))
    admin = fields.Nested("UserSchema", only=("username",))

    teams = fields.Nested("TeamSchema", many=True, only=("team_name", "user",))
    #league = fields.Nested("LeagueSchema", only=("league_name",))

league_schema = LeagueSchema()
leagues_schema = LeagueSchema(many = True)