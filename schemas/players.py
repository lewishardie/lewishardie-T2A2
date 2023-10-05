from main import ma
from marshmallow import fields

class PlayerSchema(ma.Schema):


    class Meta:
        fields = (
            "id",
            "first_name",
            "last_name",
            "nfl_team",
            "position",
            "is_available",
        )
        
    # admin_league = fields.Nested("LeagueSchema", exclude=("users",))
    
    # leagues = fields.List(fields.Nested("LeagueSchema", only=("league_name", "teams.team_name")))
    
    # teams = fields.Nested("TeamSchema", many=True, exclude=("user", "league"))

    leagues = fields.Nested("LeagueSchema", only=("id", "league_name"))
    rosters = fields.Nested("RosterSchema", only=("id", "position"), many=True)

player_schema = PlayerSchema()
players_schema = PlayerSchema(many = True)