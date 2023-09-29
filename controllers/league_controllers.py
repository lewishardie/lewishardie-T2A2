from flask import Blueprint, jsonify, request

from main import db
from models.leagues import League
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
def create_leagues():
    league_json = league_schema.load(request.json)
    league = League(**league_json)
    db.session.add(league)
    db.session.commit()

    return jsonify(league_schema.dump(league))