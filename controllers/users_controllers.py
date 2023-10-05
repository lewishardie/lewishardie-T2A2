from flask import Blueprint, jsonify, request, abort
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
# from sqlalchemy.exc import IntegrityError, DataError
from marshmallow.exceptions import ValidationError

from main import db
from models.users import User
from schemas.users import user_schema, users_schema

# /user
users = Blueprint('user', __name__, url_prefix="/user")

@users.errorhandler(ValidationError)
def key_error_handler(e):
    return jsonify({"error": f"Validation Error - `{e}`"}), 400

# /users
@users.route("/", methods=["GET"])
def get_users():
    q = db.select(User)
    users = db.session.scalars(q)

    return jsonify(users_schema.dump(users)), 200

# GET /user/user_id - get a user with an ID and authorisation
@users.route("/<int:user_id>", methods=["GET"])
@jwt_required()
def get_user(user_id):
    # Protected to registered users; ensure the user is authenticated to access this endpoint.
    current_user_id = get_jwt_identity()
    
    # Check if the current user is authorized to access this user's data
    if current_user_id != user_id:
        return jsonify(message=f"'{user_id}' is not authorized"), 401

    q = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(q)
    
    if user:
        response = user_schema.dump(user)
        return jsonify(response), 200
    else:
        return jsonify(message=f"User with id='{user_id}' not found"), 404

# PUT /user/user_id - update a user with an ID and authorisation
@users.route("/<int:user_id>", methods=["PUT"])
@jwt_required()
def update_users(user_id):
    # Protected to registered users; ensure the user is authenticated to access this endpoint.
    current_user_id = get_jwt_identity()

    # Check if the current_user_id is authorized to access this user's data
    if current_user_id != user_id:
        return jsonify(message=f"'{user_id}' is not authorized"), 401
    
    # Query the database to select data from the User table with the ID from the request
    q = db.select(User).filter_by(id=user_id)
    # Tell the query to retireve a single entry from the User table
    user = db.session.scalar(q)
    # Serialize the user data and store it in the 'response' variable
    response = user_schema.dump(user)

    # If a user is found and serialized
    if response:
        # Parse the JSON data and update the user properties
        user_json = user_schema.load(request.json, partial=True)
        # user = User(**user_json)
        if "username" in user_json:
            user.username = user_json["username"]
        if "first_name" in user_json:
            user.first_name = user_json["first_name"]
        if "last_name" in user_json:
            user.last_name = user_json["last_name"]
        if "email" in user_json:
            user.email = user_json["email"]   
        if "password" in user_json:
            user.password in user_json["password"]

        db.session.commit()
        # Return a JSON dump of the updated details
        return jsonify(user_schema.dump(user)), 200
    # If no user is found, return a JSON response with an error message
    if not response:
        return jsonify(message=f"User with id='{user_id}' not found"), 404


# DELETE /user/user_id - delete a user with an ID and authorisation
@users.route("/<int:user_id>", methods=["DELETE"])
@jwt_required()
def delete_users(user_id):
    # Protected to registered users; ensure the user is authenticated to access this endpoint.
    current_user_id = get_jwt_identity()

    # Check if the current_user_id is authorized to access this user's data
    if current_user_id != user_id:
        return jsonify(message=f"'{user_id}' is not authorized"), 401

    q = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(q)
    response = user_schema.dump(user)

    if response:
        db.session.delete(user)
        db.session.commit()
        return jsonify(message=f"User with the id=`{user_id}` has been deleted"), 200

    return jsonify(message=f"User with id='{user_id}' not found"), 404