from main import ma
from marshmallow import fields

class RosterSchema(ma.Schema):

    class Meta:
        fields = (
            "id",
            "roster_slot", 
            "team_id",
            "player_id",
        )

    team = fields.Nested("TeamSchema", only=("id", "team_name"))
    # player_id = fields.Int()

roster_schema = RosterSchema()
rosters_schema = RosterSchema(many = True)