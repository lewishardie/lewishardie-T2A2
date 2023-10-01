from main import ma
# from marshmallow import fields

class LeagueSchema(ma.Schema):

    class Meta:
        fields = (
            "id", 
            "league_name", 
            "description", 
            "max_players_per_team", 
            "max_teams", 
            "max_bench", 
            "user_id",
        )

league_schema = LeagueSchema()
leagues_schema = LeagueSchema(many = True)