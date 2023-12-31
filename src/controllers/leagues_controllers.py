from flask import Blueprint, jsonify, request, abort
from flask_jwt_extended import jwt_required, get_jwt_identity

from main import db
from models import League, User, Team
from schemas.leagues import league_schema, leagues_schema
from schemas.teams import team_schema, teams_schema


# /league
leagues = Blueprint('leagues', __name__, url_prefix="/leagues")

# GET /leagues - get all leagues
@leagues.route("/", methods=["GET"])
def get_leagues():
    # Query the database to select all data from League table
    q = db.select(League)
    # Tell the query to retireve multiple entries from the League table
    leagues = db.session.scalars(q)
    # Return a json response containing the serialised leagues data
    return jsonify(leagues_schema.dump(leagues)), 200

# POST /leagues - post/create a league
@leagues.route("/", methods=["POST"])
@jwt_required()
def create_leagues():
    # Protected to registered users; ensure the user is authenticated to access this endpoint.
    current_user_id = get_jwt_identity()
    # Load the League data from the request JSON
    league_json = league_schema.load(request.json, partial=True)
    # Create a new League instance with the loaded data
    league = League(**league_json)
    # Assign current user that's creating the league as admin
    league.admin_id = current_user_id
    
    db.session.add(league)
    db.session.commit()

    return jsonify(league_schema.dump(league)), 201

# GET /leagues/league_id - get a league with an ID
@leagues.route("/<int:league_id>", methods = ["GET"])
def get_league(league_id):
    # Query the database to retrieve data from the League table with the provided ID
    q = db.select(League).filter_by(id=league_id)
    # Retireve a single entry from the League table
    league = db.session.scalar(q)
    # Serialise the league data and store it in the 'response' variable
    response = league_schema.dump(league)

    # If a league is found, serialise the data and return as a JSON response
    if response:
        return jsonify(response), 200
    # If no league is found, return a JSON response with an error message
    return jsonify(message=f"league with ID = '{league_id}' not found"), 404

# DELETE /leagues/league_id - delete a league with an ID and authorisation
@leagues.route("/<int:league_id>", methods=["DELETE"])
@jwt_required()
def delete_league(league_id):
    # Protected to registered users, ensure the user is authenticated to access this endpoint
    current_user_id = get_jwt_identity()
    # Query the database to select all data from the League table with the ID from the request
    q = db.select(League).filter_by(id=league_id)
    # Tell the query to retireve a single entry from the League table
    league = db.session.scalar(q)
    
    # If a league is found
    if league:
        # If the current user is the admin of the league
        if league.admin_id == current_user_id:
            # Delete the league from the database
            db.session.delete(league)
            db.session.commit()
            # Return a message confirming the deletion of the league
            return jsonify(message=f"league with the id=`{league_id}` has been deleted"), 200
        else:
            # Current user isn't authorised to delete the league
            return jsonify(message="You are not authorised to delete this league."), 401
    # If no league is found, return a JSON response with an error message
    else:
        return jsonify(message=f"league with id='{league_id}' not found"), 404
    

# PUT /leagues/league_id - update a league with an ID and authorisation
@leagues.route("/<int:league_id>", methods=["PUT"])
@jwt_required()
def update_league(league_id):
    # Protected to registered users; ensure the user is authenticated to access this endpoint.
    current_user_id = get_jwt_identity()
    # Query the database to select all data from the League table with the ID from the request
    q = db.select(League).filter_by(id=league_id)
    # Tell the query to retireve a single entry from the League table    
    league = db.session.scalar(q)
    # Serialise the league data and store it in the 'response' variable
    response = league_schema.dump(league)

    # If a league is found and serialised.
    if response:
        # Check if the current user is the admin of the league
        if league.admin_id == current_user_id:
            # Parse the JSON data and update the league properties
            league_json = league_schema.load(request.json, partial=True)
            # Not every property needs to be updated as partial = True
            if "league_name" in league_json:
                league.league_name = league_json["league_name"]
            if "description" in league_json:
                league.description = league_json["description"]
            if "max_player_per_team" in league_json:
                league.max_player_per_team = league_json["max_player_per_team"]
            if "max_teams" in league_json:
                league.max_teams = league_json["max_teams"]

            db.session.commit()
            # Return a JSON dump of the updated details
            return jsonify(league_schema.dump(league)), 200
        else:
            # Current user isn't authorised to update this league
            return jsonify(message="You are not authorised to update this league."), 401
    else:
        # If no league is found, return a JSON response with an error message
        return jsonify(message=f"Cannot update league with id={league_id}. Not found"), 404  

# POST /leagues/join/league_id - join a specific league with ID, when the user is authenticated, and the league isn't full
@leagues.route("/join/<int:league_id>", methods=["POST"])
@jwt_required()
def join_league(league_id):
    # Protected to registered users; ensure the user is authenticated to access this endpoint.
    current_user_id = get_jwt_identity()
    
    # Check if the league exists
    q = db.select(League).filter_by(id=league_id)
    # Tell the query to retrieve a single entry from the League table    
    league = db.session.scalar(q)
    # If league doesn't exist return error message
    if not league:
        return jsonify(message=f"League with id='{league_id}' not found"), 404
    
    # Check if the user is already in the league
    user_in_league = db.session.query(User).\
    join(User.teams).\
    filter(Team.league_id == league_id).\
    filter(User.id == current_user_id).first()

    if user_in_league:
        return jsonify(message="You have already joined this league."), 400
    
    # Check to see if league isn't full
    if len(league.teams) > league.max_teams:
        return jsonify(message="This league is full. You cannot join."), 400

    # Parse the JSON data and update the league properties
    team_json = team_schema.load(request.json)
    # Create a new Team instance with the loaded data
    team = Team(**team_json)
    team.user_id = current_user_id
    team.league_id = league_id

    db.session.add(team)
    db.session.commit()
    # Return a JSON dump of the updated details
    return jsonify(team_schema.dump(team)), 201

# GET /leagues/league_id/team/team_id - view a team_id thats in a league_id
@leagues.route("/<int:league_id>/team/<int:team_id>", methods=["GET"])
@jwt_required()
def get_specific_tea(league_id, team_id):
    # Protected to registered users; ensure the user is authenticated to access this endpoint.
    current_user_id = get_jwt_identity()

    # Query the database to select to see if the league exists
    league = db.session.query(League).filter_by(id=league_id).first()
    # If the league doesn't exist, return an error message
    if not league:
        return jsonify(message=f"League with id='{league_id}' not found"), 404

    # Query the database to check if the user is already in the league and is part of the specified team
    team = db.session.query(Team).filter_by(id=team_id, league_id=league_id, user_id=current_user_id).first()
    
    # If a team is found, serialise the data and return it as JSON
    if team:
        response = team_schema.dump(team)
        return jsonify(response), 200
    else:
        # Current user isn't authorised to view this team
        return jsonify(message="You are not authorised to view this team."), 401