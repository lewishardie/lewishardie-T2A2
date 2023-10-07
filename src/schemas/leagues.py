# Import necessary modules and classes from 'main' and 'marshmallow'
from main import ma
from marshmallow import fields

# Define the 'LeagueSchema' class for serializing and deserializing 'League' model data
class LeagueSchema(ma.Schema):
    
    class Meta:
        # Define the fields to include in the serialized output
        fields = (
            "id", 
            "league_name", 
            "description", 
            "max_players_per_team", 
            "max_teams",  
            "commissioner",
            "teams",
        )
    # Define nested fields and their serialization options
    users = fields.Nested("UserSchema", only=("username", "id"), exclude=("leagues",))
    commissioner = fields.Nested("UserSchema", only = ("username", "id"), back_populates='admin_league')

    teams = fields.Nested("TeamSchema", many=True, only=("team_name", "user"), exclude=("user.id",))
    #league = fields.Nested("LeagueSchema", only=("league_name",))

# Create an instance of 'LeagueSchema' for single 'League' serialization
league_schema = LeagueSchema()
leagues_schema = LeagueSchema(many = True)