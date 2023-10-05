from main import ma
from marshmallow import fields
from marshmallow.validate import Length

class UserSchema(ma.Schema):
    # username = fields.String(required=True, validate=Length(min=1, error="username cannot be blank"))
    # email = fields.String(required=True)

    class Meta:
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "password", # delete when not needed
            "leagues",
            "admin_league",
        )
        
    admin_league = fields.Nested("LeagueSchema")
    
    leagues = fields.List(fields.Nested("LeagueSchema", only=("league_name", "teams.team_name")))
    
    teams = fields.Nested("TeamSchema", many=True, exclude=("user", "league"))

user_schema = UserSchema()
users_schema = UserSchema(many = True)

