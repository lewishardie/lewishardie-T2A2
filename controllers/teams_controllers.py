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

# @teams.route("/<int:team_id>", methods=["POST"])
# def delete_task(task_id: int):
#     q = db.select(Task).filter_by(id=task_id)
#     task = db.session.scalar(q)
#     response = task_schema.dump(task)

#     if response:
#         db.session.delete(task)
#         db.session.commit()
#         return jsonify(message=f"Task with id=`{task_id}` deleted successfully!")

#     return jsonify(message=f"Cannot delete task with id=`{task_id}`. Not found")

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