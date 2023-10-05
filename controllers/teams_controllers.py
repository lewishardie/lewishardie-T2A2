from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity


from main import db
from models import League, User, Team
from schemas.teams import team_schema, teams_schema

teams = Blueprint("team", __name__, url_prefix = "/team")

@teams.route("/", methods=["GET"])
def get_teams():
    q = db.select(Team)
    teams = db.session.scalars(q)
    
    return jsonify(teams_schema.dump(teams))



# @teams.route("/join/<int:league_id>", methods=["POST"])
# @jwt_required()
# def join_league(league_id):
#     current_user_id = get_jwt_identity()

#     # Check if the league exists and is not full
#     league = db.select(League).filter_by(id=league_id)

#     if not league:
#         return jsonify(message=f"League with id='{league_id}' not found"), 404

#     if len(league.teams) >= league.max_teams:
#         return jsonify(message="This league is full. You cannot join."), 400
    
#     team_json = team_schema.load(request.json)
#     # Create a new League instance with the loaded data
#     team = Team(**team_json)
#     # Create a new League instance with the loaded data
#     team.user_id = current_user_id
#     team.league_id = league_id
    
#     db.session.add(team)

#     db.session.commit()

#     return jsonify(team_schema.dump(league))



# @teams.route("/<int:team_id>", methods=["PUT"])
# def update_team(team_id: int):
#     q = db.select(Team).filter_by(id=team_id)
#     team = db.session.scalar(q)
#     response = team_schema.dump(team)

#     if response:
#         team_json = team_schema.load(request.json)
#         team.name = team_json["name"]
#         team.description = team_json["description"]
#         team.due_date = team_json["due_date"]
#         team.completed_at = team_json.get("completed_at")
#         team.user_id = team_json["user_id"]
#         db.session.commit()
#         return jsonify(team_schema.dump(team))

#     return jsonify(message=f"Cannot update team with id=`{team_id}`. Not found")