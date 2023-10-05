from main import ma
from marshmallow import fields
from marshmallow.validate import Length

class UserSchema(ma.Schema):

    class Meta:
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
        
    admin_league = fields.Nested("LeagueSchema", back_populates='commissioner')
    leagues = fields.List(fields.Nested("LeagueSchema", only=("league_name", "teams.team_name")))
    teams = fields.Nested("TeamSchema", many=True, exclude=("id", "league"))

user_schema = UserSchema()
users_schema = UserSchema(many = True)

