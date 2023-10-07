from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager


bcrypt = Bcrypt()
db = SQLAlchemy()
ma = Marshmallow()
jwt = JWTManager()


def init_app():
    # create flask app instance
    app = Flask(__name__)

    # app config
    app.config.from_object("config.app_config")
    app.json.sort_keys = False
    # connect to DB
    db.init_app(app)

    # connect schemas
    ma.init_app(app)
    
    # creating 
    bcrypt.init_app(app)
    jwt.init_app(app)

    # connect CLI commands -> blueprint
    from commands import db_commands
    app.register_blueprint(db_commands)
    
    # from controllers import users, leagues, auth, teams, players
    # app.register_blueprint(users)
    # app.register_blueprint(leagues, url_prefix="/leagues")
    # app.register_blueprint(auth)
    # app.register_blueprint(teams, url_prefix="/leagues/<int:league_id>/teams")
    # app.register_blueprint(players)

    # connect blueprint controllers
    from controllers import registered_controllers

    for controller in registered_controllers:
        app.register_blueprint(controller)

    return app