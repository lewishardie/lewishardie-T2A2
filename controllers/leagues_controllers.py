from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity


from main import db
from models import League, User
from schemas.leagues import league_schema, leagues_schema

# /league
leagues = Blueprint('league', __name__, url_prefix="/league")

# /leagues
@leagues.route("/", methods=["GET"])
def get_leagues():
    q = db.select(League)
    leagues = db.session.scalars(q)

    return jsonify(leagues_schema.dump(leagues))

# create leagues
@leagues.route("/", methods=["POST"])
@jwt_required()
def create_leagues():
    # get the id from jwt_required
    email = get_jwt_identity()
    stmt = db.select(User).filter_by(email=email)
    user = db.session.scalar(stmt)

    # create new league
    league_json = league_schema.load(request.json)
    league = League(**league_json)
    # league = League()
    # league.name = league_json["name"]
    # league.description = league_json["description"]
    # league.max_players_per_team = league_json["max_players_per_team"]
    # league.max_teams = league_json["max_teams"]
    # league.max_bench = league_json["max_bench"]
    league.user_id = user.id


    db.session.add(league)
    db.session.commit()

    return jsonify(league_schema.dump(league))

# select a specific league
@leagues.route("/<int:league_id>", methods = ["GET"])
def get_league(league_id: int):
    q = db.select(League).filter_by(id=league_id)
    league = db.session.scalar(q)
    response = league_schema.dump(league)

    if response:
        return jsonify(response)
    
    return jsonify(message=f"league with ID = '{league_id}' not found")

# /league/<id> -> Updating a league with id
@leagues.route("/<int:league_id>", methods=["PUT"])
@jwt_required()
def update_league(league_id: id):
    league_id = get_jwt_identity()
    q = db.select(League).filter_by(id=league_id)
    league = db.session.scalar(q)
    response = league_schema.dump(league)

    if response:
        league_json = league_schema.load(request.json)
        # league = League()
        league.league_name = league_json["league_name"]
        league.description = league_json["description"]
        league.max_players_per_team = league_json["max_players_per_team"]
        league.max_teams = league_json["max_teams"]
        league.max_bench = league_json["max_bench"]
        #league.user_id = league_json["user_id"]

        db.session.commit()
        return jsonify(league_schema.dump(league))

    return jsonify(message=f"Cannot update league with id=`{league_id}`. Not found")