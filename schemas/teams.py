# Import necessary modules and classes from 'main' and 'marshmallow'
from main import ma
from marshmallow import fields

# Define the 'TeamSchema' class for serializing and deserializing 'Team' model data
class TeamSchema(ma.Schema):

    class Meta:
        # Define the fields to include in the serialized output
        fields = (
            "id",
            "team_name", 
            "user",
            "league",
            "roster",
        )

    # Define nested fields and their serialization options
    user = fields.Nested("UserSchema", only=("username",)) 
    league = fields.Nested("LeagueSchema", only=("league_name",))
    roster = fields.Nested("RosterSchema", many=True, only=("roster_slot",))
# Create an instance of 'TeamSchema' for single 'Team' serialization
team_schema = TeamSchema()
teams_schema = TeamSchema(many = True)