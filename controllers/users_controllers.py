from flask import Blueprint, jsonify, request

from main import db
from models.users import User
from schemas.users import user_schema, users_schema

# /user
users = Blueprint("user", __name__, url_prefix = "/users")

# /users
@users.route("/", methods = ["GET"])
def get_users():
    q = db.select(User)
    users = db.session.scalars(q)

    return jsonify(user_schema.dump(users))

