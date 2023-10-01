from flask import Blueprint, jsonify, request
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

# create users
# @users.route("/", methods=["POST"])
# def create_users():
#     user_json = user_schema.load(request.json)
#     user = User(**user_json)
#     db.session.add(user)
#     db.session.commit()

#     return jsonify(users_schema.dump(user))

#/users/<id> -> user with id
@users.route("/<int:user_id>", methods=["GET"])
def get_user(user_id: int):
    q = db.select(User).filter_by(id=user_id) #filter(User.id == id) is another option
    user = db.session.scalar(q)
    response = user_schema.dump(user)

    if response:
        return jsonify(response)

    return jsonify(message=f"User with id='{user_id}' not found")


# /users/<id> -> Updating a user with id

@users.route("/<int:user_id>", methods=["PUT"])
@jwt_required()
def update_users(user_id: id):
    user_id = get_jwt_identity()
    q = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(q)
    response = user_schema.dump(user)

    # q = db.select(User).filter_by(id=user_id)
    # user = db.session.scalar(q)
    # response = user_schema.dump(user)

    if response:
        user_json = user_schema.load(request.json)
        # user = User(**user_json)
        user.username = user_json["username"]
        user.first_name = user_json["first_name"]
        user.last_name = user_json["last_name"]
        user.email = user_json["email"]

        db.session.commit()
        return jsonify(user_schema.dump(user))

    return jsonify(message=f"User with id='{user_id}' not found")