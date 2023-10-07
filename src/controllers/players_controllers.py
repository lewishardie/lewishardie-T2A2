from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from main import db
from models import League, User, Player
from schemas.players import player_schema, players_schema

players = Blueprint("player", __name__, url_prefix = "/players")

# GET /players - get all players
@players.route("/", methods=["GET"])
def get_players():
    # Query the database to select all data from the player table
    q = db.select(Player)
    # Tell the query to retireve a multiple entry from the player table 
    players = db.session.scalars(q)
    # Return a json response containing the serialised players data
    return jsonify(players_schema.dump(players)), 200

# GET /players - get all players
@players.route("/<int:player_id>", methods=["GET"])
def get_player(player_id):
    print(type(player_id))
    print(player_id)
    # Query the database to select all data from the player table
    q = db.select(Player).filter_by(id=player_id)
    # Tell the query to retireve a multiple entry from the player table 
    player = db.session.scalar(q)
    # Return a json response containing the serialised players data
    response = player_schema.dump(player)

    # If a player is found, serialise the data and return as a JSON response
    if response:
        return jsonify(response), 200
    # If no player is found, return a JSON response with an error message
    return jsonify(message=f"player with ID = '{player_id}' not found"), 404

# GET /players/available - get all available players
@players.route("/available", methods=["GET"])
def available_players():
    # Query the database to select all available players
    q = db.select(Player).filter_by(is_available=True)
    available_players = db.session.scalars(q)
    
    # If available players are found, serialise the data and return as a JSON response
    if available_players:
        return jsonify(players_schema.dump(available_players)), 200
    else:
        # If no available players are found, return a JSON response with a message
        return jsonify(message="No available players found."), 404