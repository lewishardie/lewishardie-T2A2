from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from main import db
from models import League, User, Team, Player, Roster
from schemas.teams import team_schema, teams_schema

teams = Blueprint("teams", __name__, url_prefix="/teams")

# GET /teams - view all teams
@teams.route("/list", methods=["GET"])
def get_teams():
    # Query the database to select all data from the Team table
    q = db.select(Team)
    # Tell the query to retireve a multiple entry from the Team table 
    teams = db.session.scalars(q)
    # Return a json response containing the serialised Teams data
    return jsonify(teams_schema.dump(teams)), 200

# GET /teams/team_id - get a team with an ID
@teams.route("/<int:team_id>", methods = ["GET"])
def get_team(team_id):
    # Query the database to retrieve data from the team table with the provided ID
    q = db.select(Team).filter_by(id=team_id)
    # Retireve a single entry from the team table
    team = db.session.scalar(q)
    # Serialise the team data and store it in the 'response' variable
    response = team_schema.dump(team)

    # If a team is found, serialise the data and return as a JSON response
    if response:
        return jsonify(response), 200
    # If no team is found, return a JSON response with an error message
    return jsonify(message=f"team with ID = '{team_id}' not found"), 404

# PUT /teams/team_id - update a team with an ID and authorisation
@teams.route("/<int:team_id>", methods=["PUT"])
@jwt_required()
def update_team(team_id):
    # Protected to registered users; ensure the user is authenticated to access this endpoint.
    current_user_id = get_jwt_identity()
    # Query the database to select all data from the Team table with the ID from the request
    q = db.select(Team).filter_by(id=team_id)
    team = db.session.scalar(q)
    # Serialise the league data and store it in the 'response' variable
    response = team_schema.dump(team)

     # If a league is found and serialised.
    if response:
        # Check if the current user is the admin of the league
        if team.user_id == current_user_id:
            # Parse the JSON data and update the team properties
            team_json = team_schema.load(request.json)
            team.team_name = team_json["team_name"]

            db.session.commit()
            # Return a JSON dump of the updated details
            return jsonify(team_schema.dump(team)), 200
        else:
            # Current user isn't authorised to update this team
            return jsonify(message="You are not authorised to update this team."), 401
    else:
        # If no team is found, return a JSON response with an error message
        return jsonify(message=f"Cannot update team with id={team_id}. Not found"), 404

# DELETE /teams/team_id - delete a team with an ID and authorisation
@teams.route("/<int:team_id>", methods=["DELETE"])
@jwt_required()
def delete_team(team_id):
    # Protected to registered users; ensure the user is authenticated to access this endpoint.
    current_user_id = get_jwt_identity()
    # Query the database to select all data from the Team table with the ID from the request
    q = db.select(Team).filter_by(id=team_id)
    team = db.session.scalar(q)
    # Check if the current_user_id is authorised to access this user's data

    # Serialise the league data and store it in the 'response' variable
    response = team_schema.dump(team)

     # If a league is found and serialised.
    if response:
        # Check if the current user is the admin of the league
        if team.user_id == current_user_id:
            # Parse the JSON data and update the team properties
            db.session.delete(team)
            db.session.commit()
            # Return a JSON dump of the updated details
            return jsonify(message=f"team with the id=`{team_id}` has been deleted"), 200
        else:
            # Current user isn't authorised to update this team
            return jsonify(message="You are not authorised to delete this team."), 401
    else:
        # If no team is found, return a JSON response with an error message
        return jsonify(message=f"Cannot delete team with id={team_id}. Not found"), 404
    
# POST /teams/<int:team_id>/add/<int:player_id> - add a player to a team's roster
@teams.route("/<int:team_id>/add/<int:player_id>", methods=["POST"])
@jwt_required()
def add_player_to_roster(team_id, player_id):
    # Protected to registered users; ensure the user is authenticated to access this endpoint.
    current_user_id = get_jwt_identity()
    
    # Check if the team exists
    team = db.session.query(Team).filter_by(id=team_id).first()
    if not team:
        return jsonify(message=f"Team with id='{team_id}' not found"), 404
    
    # Check if the team is in a specific league
    league_id = team.league_id
    
    # Check if the player is available (not already in a roster)
    player = db.session.query(Player).filter_by(id=player_id).first()
    if not player:
        return jsonify(message=f"Player with id='{player_id}' not found"), 404
    
    if player.roster_id is not None:
        return jsonify(message="Player is already in a roster"), 400
    
    # Check if the user is authorised to add a player to this team (e.g., team membership)
    # Implement your authorisation logic here
    
    # Create a new roster entry for the player on the team
    roster = Roster(team_id=team_id, player_id=player_id)
    
    db.session.add(roster)
    db.session.commit()
    
    return jsonify(message="Player added to the team's roster"), 201