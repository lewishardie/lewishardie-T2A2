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

    return jsonify(users_schema.dump(users))

#/users/<id> -> user with id
@users.route("/<int:user_id>", methods=["GET"])
@jwt_required()
def get_user(user_id):
    current_user_id = get_jwt_identity()
    print(type(user_id))
    print(type(current_user_id))
    
    # Check if the current user is authorized to access this user's data
    if current_user_id != user_id:
        return jsonify(message=f"'{user_id}' is not authorized"), 401

    q = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(q)
    
    if user:
        response = user_schema.dump(user)
        return jsonify(response)
    else:
        return jsonify(message=f"User with id='{user_id}' not found"), 404
    
# @users.route("/<int:user_id>", methods=["GET"])
# @jwt_required()
# def get_user(user_id):
#     current_user_id = get_jwt_identity()
#     print(current_user_id)
#     print(user_id)
#     if current_user_id == user_id:
#         q = db.select(User).filter_by(id=user_id)
#         user = db.session.scalar(q)
#         response = user_schema.dump(user)

#         if response:
#             return jsonify(response)
#         else:
#             return jsonify(message=f"User with id='{user_id}' not found"), 404
#     else:
#         return jsonify(message=f"'{user_id}' is not authorized to access this resource"), 403

# Updating a user that has authorisation to do so

@users.route("/<int:user_id>", methods=["PUT"])
@jwt_required()
def update_users(user_id):
    # assign jwt identity to current_user_id
    current_user_id = get_jwt_identity()
    print(type(user_id))
    print(type(current_user_id))
    
    # Check if the current_user_id is authorized to access this user's data
    if current_user_id != user_id:
        return jsonify(message=f"'{user_id}' is not authorized"), 401
    
    # search the database for the user_id
    q = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(q)    
    response = user_schema.dump(user)

    # if the user exsists proceed to update
    if response:
        user_json = user_schema.load(request.json)
        # user = User(**user_json)
        user.username = user_json["username"]
        user.first_name = user_json["first_name"]
        user.last_name = user_json["last_name"]
        user.email = user_json["email"]

        db.session.commit()
        return jsonify(user_schema.dump(user))
    
    if not response:
        return jsonify(message=f"User with id='{user_id}' not found")

# Delete a user that has authorisation to do so

@users.route("/<int:user_id>", methods=["DELETE"])
@jwt_required()
def delete_users(user_id):
    # assign jwt identity to current_user_id
    current_user_id = get_jwt_identity()
    print(type(user_id))
    print(type(current_user_id))

    # Check if the current_user_id is authorized to access this user's data
    if current_user_id != user_id:
        return jsonify(message=f"'{user_id}' is not authorized"), 401

    q = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(q)
    response = user_schema.dump(user)

    if response:
        db.session.delete(user)
        db.session.commit()
        return jsonify(message=f"User with the id=`{user_id}` has been deleted")

    return jsonify(message=f"User with id='{user_id}' not found")