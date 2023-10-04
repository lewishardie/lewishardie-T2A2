from flask import Blueprint, jsonify, request, abort
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
    user_id = get_jwt_identity()
    print(f"Current User: {user_id}, League ID: {get_jwt_identity}")
    league_json = league_schema.load(request.json)

    league = League(**league_json)
    league.admin_id = user_id
    
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

@leagues.route("/<int:league_id>", methods=["DELETE"])
@jwt_required()
def delete_league(league_id):
    # assign jwt identity to current_user_id
    current_user_id = get_jwt_identity()

    q = db.select(League).filter_by(id=league_id)
    league = db.session.scalar(q)
    response = league_schema.dump(league)

    if response:
        # Check if the current user is the admin of the league
        if league.admin_id == current_user_id:
            db.session.delete(league)
            db.session.commit()
            return jsonify(message=f"league with the id=`{league_id}` has been deleted")
        else:
            return jsonify(message="You are not authorized to delete this league."), 401
    else:
        return jsonify(message=f"league with id='{league_id}' not found")

# /league/<id> -> Updating a league as league admin
@leagues.route("/<int:league_id>", methods=["PUT"])
@jwt_required()
def update_league(league_id):
    # assign jwt identity to current_user_id
    current_user_id = get_jwt_identity()

    # Query the league by ID
    q = db.select(League).filter_by(id=league_id)
    league = db.session.scalar(q)
    print(f"League ID: {league_id}, Current User ID: {current_user_id}")

    if league:
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

            return jsonify(league_schema.dump(league))
        else:
            return jsonify(message="You are not authorized to update this league."), 401
    else:
        return jsonify(message=f"Cannot update league with id={league_id}. Not found"), 404  
    
      
    # # authorization to update league
    # current_user = get_jwt_identity()

    # # debug
    # print(f"Current User: {current_user}, League ID: {league_id}")
    
    # q = db.select(League).filter_by(id=league_id)
    # league = db.session.scalar(q)
    # #debug
    # print(f"League Admin ID: {league.admin_id}")

    # response = league_schema.dump(league)

    # # league_json = league_schema.load(request.json)
    # # league = League(**league_json)

    # if league.admin_id != current_user:
    #    print(f"Unauthorized: Admin ID ({league.admin_id}) does not match Current User ({current_user})")
    #    return jsonify(message=f"{current_user} You are not authorized to update this league."), 401

    # if response:
    #     # request the json
    #     league_json = league_schema.load(request.json)
    #     league.league_name = league_json["league_name"]
    #     league.description = league_json["description"]
    #     league.max_players_per_team = league_json["max_players_per_team"]
    #     league.max_teams = league_json["max_teams"]
    #     league.max_bench = league_json["max_bench"]

    #     db.session.commit()
    #     return jsonify(league_schema.dump(league))

    # return jsonify(message=f"Cannot update league with id=`{league_id}`. Not found")


# @users.route("/<int:user_id>", methods=["PUT"])
# @jwt_required()
# def update_users(user_id: id):
#     user_id = get_jwt_identity()
#     q = db.select(User).filter_by(id=user_id)
#     user = db.session.scalar(q)
#     response = user_schema.dump(user)

#     if response:
#         user_json = user_schema.load(request.json)
#         # user = User(**user_json)
#         user.username = user_json["username"]
#         user.first_name = user_json["first_name"]
#         user.last_name = user_json["last_name"]
#         user.email = user_json["email"]

#         db.session.commit()
#         return jsonify(user_schema.dump(user))

#     return jsonify(message=f"User with id='{user_id}' not found")


#  --------------------------------------------------------------------------
# end point for joining a league
# @leagues.route("/join/<int:league_id>", methods=["POST"])
# @jwt_required()
# def join_league(league_id):
#     user_id = get_jwt_identity()

#     # check if the league exists and is not full
#     q = db.select(League).filter_by(id=league_id)
#     league = db.session.scalar(q)
#     response =league_schema.dump(league)
    

#     if response:
#         UserLeague.query.filter_by(user_id=user_id, league_id=league_id).first():
#         return jsonify(message="You are already a member of this league."), 400

#     if league.current_team_count >= league.max_teams:
#         return jsonify(message="This league is full and no more teams can join."), 400
    
#     user_league = UserLeague(user_id=user_id, league_id=league_id)
#     db.session.add(user_league)

#     # Update the current_team_count
#     league.current_team_count += 1

#     db.session.commit()

#     return jsonify(message="You have successfully joined the league."), 201

#     # league_json = league_schema.load(request.json)

        


#     # Check if the user is already a member of the league

    
#     # if not q:
#     #     return jsonify(message="League not found."), 404

#     return jsonify(message=f"Cannot join league with id=`{league_id}`. Not found")