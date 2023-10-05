from flask import Blueprint, jsonify, request, abort
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity


from main import db
from models import League, User, Team
from schemas.leagues import league_schema, leagues_schema
from schemas.teams import team_schema, teams_schema
from schemas.users import user_schema, users_schema

# /league
leagues = Blueprint('league', __name__, url_prefix="/league")

# /leagues
@leagues.route("/", methods=["GET"])
def get_leagues():
    # Query the database to select all data from League table
    q = db.select(League)
    # Tell the query to retireve multiple entries from the League table
    leagues = db.session.scalars(q)
    # Return a json response containing the serialised leagues data
    return jsonify(leagues_schema.dump(leagues))

# Create leagues
@leagues.route("/", methods=["POST"])
@jwt_required()
def create_leagues():
    # Protected to registered users; ensure the user is authenticated to access this endpoint.
    current_user_id = get_jwt_identity()
    # Load the League data from the request JSON
    league_json = league_schema.load(request.json)
    # Create a new League instance with the loaded data
    league = League(**league_json)
    # Create a new League instance with the loaded data
    league.admin_id = current_user_id
    
    db.session.add(league)
    db.session.commit()

    return jsonify(league_schema.dump(league))

# Getting a league with ID
@leagues.route("/<int:league_id>", methods = ["GET"])
def get_league(league_id: int):
    # Query the database to retrieve data from the League table with the provided ID
    q = db.select(League).filter_by(id=league_id)
    # Retireve a single entry from the League table
    league = db.session.scalar(q)
    # Serialize the league data and store it in the 'response' variable
    response = league_schema.dump(league)

    # If a league is found and serialized, return it as a JSON response
    if response:
        return jsonify(response)
    # If no league is found, return a JSON response with an error message
    return jsonify(message=f"league with ID = '{league_id}' not found")

# Deleting a league with ID and authorization
@leagues.route("/<int:league_id>", methods=["DELETE"])
@jwt_required()
def delete_league(league_id):
    # Protected to registered users, ensure the user is authenticated to access this endpoint
    current_user_id = get_jwt_identity()
    # Query the database to select all data from the League table with the ID from the request
    q = db.select(League).filter_by(id=league_id)
    # Tell the query to retireve a single entry from the League table
    league = db.session.scalar(q)
    
    # If a league is found and serialized
    if league:
        # If the current user is the admin of the league
        if league.admin_id == current_user_id:
            # Delete the league from the database
            db.session.delete(league)
            db.session.commit()
            # Return a message confirming the deletion of the league
            return jsonify(message=f"league with the id=`{league_id}` has been deleted")
        else:
            # Current user isn't authorised to delete the league
            return jsonify(message="You are not authorized to delete this league."), 401
    # If no league is found, return a JSON response with an error message
    else:
        return jsonify(message=f"league with id='{league_id}' not found")
    

# Updating a league with ID and authorization
@leagues.route("/<int:league_id>", methods=["PUT"])
@jwt_required()
def update_league(league_id):
    # Protected to registered users; ensure the user is authenticated to access this endpoint.
    current_user_id = get_jwt_identity()
    # Query the database to select all data from the League table with the ID from the request
    q = db.select(League).filter_by(id=league_id)
    # Tell the query to retireve a single entry from the League table    
    league = db.session.scalar(q)
    # Serialize the league data and store it in the 'response' variable
    response = league_schema.dump(league)

    # If a league is found and serialized.
    if response:
        # Check if the current user is the admin of the league
        if league.admin_id == current_user_id:
            # Parse the JSON data and update the league properties
            league_json = league_schema.load(request.json)
            league.league_name = league_json["league_name"]
            league.description = league_json["description"]
            league.max_players_per_team = league_json["max_players_per_team"]
            league.max_teams = league_json["max_teams"]
            league.max_bench = league_json["max_bench"]

            db.session.commit()
            # Return a message confirming league has been updated
            return jsonify(league_schema.dump(league))
        else:
            # Current user isn't authorised to update this league
            return jsonify(message="You are not authorized to update this league."), 401
    else:
        # If no league is found, return a JSON response with an error message
        return jsonify(message=f"Cannot update league with id={league_id}. Not found"), 404  

@leagues.route("/join/<int:league_id>", methods=["POST"])
@jwt_required()
def join_league(league_id):
    current_user_id = get_jwt_identity()
    
    # Check if the league exists and is not full
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
        return jsonify(message="You have already joined this league."), 401
    
    # Check to see if league isn't full
    if len(league.teams) > league.max_teams:
        return jsonify(message="This league is full. You cannot join."), 400

    # Parse the JSON data and update the league properties
    team_json = team_schema.load(request.json)
    # Create a new Team instance with the loaded data
    team = Team(**team_json)
    # Create a new Team instance with the loaded data
    team.user_id = current_user_id
    team.league_id = league_id

    db.session.add(team)
    db.session.commit()
    
    return jsonify(team_schema.dump(team))

