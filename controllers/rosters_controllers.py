from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from main import db
from models import Roster
from schemas.rosters import roster_schema, rosters_schema

rosters = Blueprint("roster", __name__, url_prefix = "/rosters")

# GET /roster - get all roster
@rosters.route("/", methods=["GET"])
def get_rosters():
    # Query the database to select all data from the player table
    q = db.select(Roster)
    # Tell the query to retireve a multiple entry from the player table 
    rosters = db.session.scalars(q)
    # Return a json response containing the serialised players data
    return jsonify(rosters_schema.dump(rosters)), 200

# GET /roster with ID
@rosters.route("/<int:roster_id>", methods=["GET"])
def get_roster(roster_id):
    # Query the database to select all data from the player table
    q = db.select(Roster).filter_by(id=roster_id)
    # Tell the query to retireve a multiple entry from the player table 
    roster = db.session.scalar(q)
    
    response = roster_schema.dump(roster)

    # If a team is found, serialise the data and return as a JSON response
    if response:
        return jsonify(response), 200
    # If no team is found, return a JSON response with an error message
    return jsonify(message=f"team with ID = '{roster_id}' not found"), 404