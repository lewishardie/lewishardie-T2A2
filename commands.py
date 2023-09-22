from flask import Blueprint
from datetime import datetime
from flask_bcrypt import Bcrypt

from main import db
from models import User #League

db_commands = Blueprint("db", __name__)

@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("tables created")

@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("tables dropped")

@db_commands.cli.command("seed")
def seed_db():

    user1 = User(
        username = "hardcores",
        first_name = "lewis",
        last_name = "hardie",
        email = "lewishardie@gmail.com",
        password = "123456"
    )

    # add all user objets to db
    db.session.add_all([
        user1
        ])

    # commit db for users
    db.session.commit()


    # # create league object
    # league1 = League(
    #     name = "League Test",
    #     description = "this is a test for a league",
    #     start_date = "start of the nfl season",
    #     end_date = "end of nfl season",
    #     max_players_per_team = 16,
    #     max_teams = 12,
    #     max_bench = 6,
    #     commissioner = True
    # )

    # # add league object to db
    # db.session.add_all([
    #     league1
    # ])

    # # commit db for league
    # db.session.commit()

    # log if seed succeeds
    print("Database has been seeded")