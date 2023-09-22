from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
db = SQLAlchemy()
ma = Marshmallow()

# app = Flask(__name__)

# @app.route('/')
# def welcome():
#     return "Welcome"

def init_app():
    # create flask app instance
    app = Flask(__name__)

    # app config
    app.config.from_object("config.app_config")

    # connect to DB
    db.init_app(app)

    # connect schemas
    ma.init_app(app)

    # connect CLI commands -> blueprint
    from commands import db_commands
    app.register_blueprint(db_commands)

    # connect blueprint controllers
    from controllers import registered_controllers

    for controller in registered_controllers:
        app.register_blueprint(controller)

    return app