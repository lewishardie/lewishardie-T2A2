# Import necessary modules and classes from 'main' and 'marshmallow'
from main import ma
from marshmallow import fields

# Define the 'UserSchema' class for serializing and deserializing 'User' model data
class UserSchema(ma.Schema):

    class Meta:
        # Define the fields to include in the serialized output
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "leagues",
        )
        load_only = ["password"]
     # Define nested fields and their serialization options
    admin_league = fields.Nested("LeagueSchema", back_populates='commissioner')
    leagues = fields.List(fields.Nested("LeagueSchema", only=("league_name", "teams.team_name")))
    teams = fields.Nested("TeamSchema", many=True, exclude=("id", "league"))
# Create an instance of 'UserSchema' for single 'User' serialization
user_schema = UserSchema()
users_schema = UserSchema(many = True)

