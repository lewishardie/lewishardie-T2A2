from main import ma
# from marshmallow import fields

class LeagueSchema(ma.Schema):

    class Meta:
        fields = "name", "description", "start_date", "end_date", "max_players_per_team", "max_teams", "max_bench", "commissioner"

league_schema = LeagueSchema()
leagues_schema = LeagueSchema(many = True)