from flask import Blueprint, request, jsonify, abort
from sqlalchemy.exc import IntegrityError
from datetime import timedelta
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity


from main import db, bcrypt
from models.users import User
from schemas.users import user_schema, users_schema

# Authentication blueprint

auth = Blueprint("auth", __name__, url_prefix = "/auth")

# Register Authentication

@auth.errorhandler(IntegrityError)
def integrity_error_handler(e):
    return jsonify({"error": f"Integrity Error - `{e}`"}), 400


@auth.route("/register", methods = ["POST"])
def register_user():
    # Load the user data from the request JSON
    user_json = user_schema.load(request.json)
    # Query the database to retrieve data from the User table with the provided email
    q = db.select(User).filter_by(email=user_json["email"])
    # Retireve a single entry from the User table
    user = db.session.scalar(q)
    # If a email is already in table, return an abort message to inform the user
    if user:
        return abort(400, description = "Email already registered")
    
    # Create a new User instance with the loaded data
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
    # Create expiry date for the access token
    expiry = timedelta(days=1)
    # Create access token for authorisation
    access_token = create_access_token(identity=user.id, expires_delta=expiry)
    # Return a message confirming user has successfully been registered
    return jsonify({"user": user.username, "message": "Success, you have been registered", "token": access_token }), 201 # "user":user.email, 

# Login authentication
@auth.route("/login", methods=["POST"])
# @jwt_required
def login_user():

    email = request.json["email"]
    password = request.json["password"]
    # Query the database to retrieve data from the User table with the provided email
    q = db.select(User).filter_by(email=email)
    # Retireve a single entry from the User table
    user = db.session.scalar(q)
    # Check the if the entry exists and if the password matches
    if not user or not bcrypt.check_password_hash(user.password, password):
        return abort(400, description = "Incorrect username or password")
    # Create expiry date for the access token
    expiry = timedelta(days=1)
    # Create access token for authorisation
    access_token = create_access_token(identity=user.id, expires_delta=expiry)
    # Return a message confirming user has successfully been logged in
    return jsonify({"message": "Success, you have logged in", "email": user.email, "token": access_token}), 201

