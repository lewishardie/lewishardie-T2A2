from flask import Blueprint
from datetime import date

from main import db, bcrypt
from models import User, League

db_commands = Blueprint("db", __name__)

@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("tables created")

@db_commands.cli.command("seed")
def seed_db():

    user1 = User(
        username = "hardcores",
        first_name = "lewis",
        last_name = "hardie",
        email = "lewishardie@gmail.com",
        password = bcrypt.generate_password_hash("123456").decode("utf-8")
    )

    # add all user objets to db
    db.session.add_all([
        user1
        ])

    # commit db for users
    db.session.commit()

    # create league object
    league1 = League(
        name = "League Test",
        description = "this is a test for a league",
        start_date = date(2024, 9, 1),
        end_date = date(2025, 2, 20),
        max_players_per_team = 16,
        max_teams = 12,
        max_bench = 6,
        commissioner = True
    )

    # add league object to db
    db.session.add_all([
        league1
    ])

    # commit db for league
    db.session.commit()

    # log if seed succeeds
    print("Database has been seeded")

@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("tables dropped")

    # seed nfl tables and player tables from the get go?