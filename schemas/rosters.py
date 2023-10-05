# Import necessary modules and classes from 'main' and 'marshmallow'
from main import ma
from marshmallow import fields

# Define the 'RosterSchema' class for serializing and deserializing 'Roster' model data
class RosterSchema(ma.Schema):

    class Meta:
        # Define the fields to include in the serialized output
        fields = (
            "id",
            "roster_slot", 
            "team_id",
            "player_id",
        )
    # Define nested fields and their serialization options
    team = fields.Nested("TeamSchema", only=("id", "team_name"))

# Create an instance of 'RosterSchema' for single 'Roster' serialization
roster_schema = RosterSchema()
rosters_schema = RosterSchema(many = True)