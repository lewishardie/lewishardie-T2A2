from main import ma
from marshmallow import fields

class TeamSchema(ma.Schema):

    class Meta:
        fields = (
            "id",
            "team_name", 
            "user",
            "league",
            "roster",
        )

    # user_id = fields.Int()
    user = fields.Nested("UserSchema", only=("username",)) 
    league = fields.Nested("LeagueSchema", only=("league_name",))
    roster = fields.Nested("RosterSchema", many=True, only=("roster_slot",))

team_schema = TeamSchema()
teams_schema = TeamSchema(many = True)