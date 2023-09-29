from main import ma
# from marshmallow import fields

class UserSchema(ma.Schema):

    class Meta:
        fields = "id", "username", "first_name", "last_name", "email", "password"

user_schema = UserSchema()
users_schema = UserSchema(many = True)

