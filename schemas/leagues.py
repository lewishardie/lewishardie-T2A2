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
            "commissioner",
            "teams",
        )

    users = fields.Nested("UserSchema", only=("username", "id"), exclude=("leagues",))
    commissioner = fields.Nested("UserSchema", only = ("username", "id"), back_populates='admin_league')

    teams = fields.Nested("TeamSchema", many=True, only=("team_name", "user"), exclude=("user.id",))
    #league = fields.Nested("LeagueSchema", only=("league_name",))

league_schema = LeagueSchema()
leagues_schema = LeagueSchema(many = True)