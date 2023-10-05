from flask import Blueprint, request, jsonify, abort
from sqlalchemy.exc import IntegrityError
from datetime import timedelta
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity


from main import db, bcrypt
from models.users import User
from schemas.users import user_schema, users_schema

# Authentication blueprint

auth = Blueprint("auth", __name__, url_prefix = "/auth")

# @auths.route("/register", methods="GET")

# Register Authentication

@auth.errorhandler(IntegrityError)
def integrity_error_handler(e):
    return jsonify({"error": f"Integrity Error - `{e}`"}), 400


@auth.route("/register", methods = ["POST"])
def register_user():
    user_json = user_schema.load(request.json)
    q = db.select(User).filter_by(email=user_json["email"])
    user = db.session.scalar(q)
    print(user_json)
    if user:
        # return an abort message to inform the user. that will end the request
        return abort( 400, description = "Email already registered")
    
    # Create User
    user = User()
    # add username
    user.username = user_json["username"]
    # Add email
    user.email = user_json["email"]
    # add the password
    user.password = bcrypt.generate_password_hash(user_json["password"]).decode("utf-8")
    # add to database
    db.session.add(user)
    db.session.commit()
    # create expiry date
    expiry = timedelta(days=1)
    # create access token
    access_token = create_access_token(identity=user.id, expires_delta=expiry)

    return jsonify({"user": user.username, "message": "Success, you have been registered", "token": access_token }), 200 # "user":user.email, 

# Login authentication
@auth.route("/login", methods=["POST"])
# @jwt_required
def login_user():

    email = request.json["email"]
    password = request.json["password"]

    q = db.select(User).filter_by(email=email)
    user = db.session.scalar(q)

    if not user or not bcrypt.check_password_hash(user.password, password):
        return abort (401, description = "Incorrect username or password")
        
    expiry = timedelta(days=1)

    access_token = create_access_token(identity=user.id, expires_delta=expiry)
        
    return jsonify({"message": "Success, you have logged in", "email": user.email, "token": access_token}), 200

