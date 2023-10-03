from main import ma
from marshmallow import fields

class TeamSchema(ma.Schema):

    class Meta:
        fields = (
            "id",
            "team_name", 
            #"starters", 
            #"bench",
            "user",
            "league",
        )

    user = fields.Nested("UserSchema", only=("username",), exclude=("leagues", "admin_league", ))
    league = fields.Nested("LeagueSchema", only=("league_name",))

team_schema = TeamSchema()
teams_schema = TeamSchema(many = True)