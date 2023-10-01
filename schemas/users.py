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
            "password",
            "leagues"
        )
        
    #leagues = fields.List(fields.Nested("LeagueSchema", exclude=("user",)))

user_schema = UserSchema()
users_schema = UserSchema(many = True)

