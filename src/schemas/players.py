# Import necessary modules and classes from 'main' and 'marshmallow'
from main import ma
from marshmallow import fields

# Define the 'PlayerSchema' class for serializing and deserializing 'Player' model data
class PlayerSchema(ma.Schema):


    class Meta:
        # Define the fields to include in the serialized output
        fields = (
            "id",
            "first_name",
            "last_name",
            "nfl_team",
            "position",
            "is_available",
        )
    # Define nested fields and their serialization options  
  
    # admin_league = fields.Nested("LeagueSchema", exclude=("users",))    
    # leagues = fields.List(fields.Nested("LeagueSchema", only=("league_name", "teams.team_name")))
    # teams = fields.Nested("TeamSchema", many=True, exclude=("user", "league"))

    leagues = fields.Nested("LeagueSchema", only=("id", "league_name"))
    rosters = fields.Nested("RosterSchema", only=("id", "position"), many=True)
# Create an instance of 'PlayerSchema' for single 'Player' serialization
player_schema = PlayerSchema()
players_schema = PlayerSchema(many = True)