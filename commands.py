from flask import Blueprint
from datetime import date

from main import db, bcrypt
from models import User, League, Team

db_commands = Blueprint("db", __name__)

@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("tables created")

@db_commands.cli.command("seed")
def seed_db():

    user1 = User(
        username = "hardcores1",
        first_name = "lewis",
        last_name = "hardie",
        email = "lewishardie1@gmail.com",
        password = bcrypt.generate_password_hash("123456").decode("utf-8"),
    )

    user2 = User(
        username = "hardcores2",
        first_name = "lewis",
        last_name = "hardie",
        email = "lewishardie2@gmail.com",
        password = bcrypt.generate_password_hash("123456").decode("utf-8"),
    )

    user3 = User(
        username = "hardcores3",
        first_name = "lewis",
        last_name = "hardie",
        email = "lewishardie3@gmail.com",
        password = bcrypt.generate_password_hash("123456").decode("utf-8"),
    )

    user4 = User(
        username = "hardcores4",
        first_name = "lewis",
        last_name = "hardie",
        email = "lewishardie4@gmail.com",
        password = bcrypt.generate_password_hash("123456").decode("utf-8"),
    )

    # add all user objets to db
    db.session.add_all([
        user1, user2, user3, user4
        ])

    # commit db for users
    db.session.commit()

    # create league object
    league1 = League(
        league_name = "League Test 1",
        description = "this is a test for a league",
        # start_date = date(2024, 9, 1),
        # end_date = date(2025, 2, 20),
        max_players_per_team = 16,
        max_teams = 12,
        max_bench = 6,
        admin_id = user1.id
    )

    league2 = League(
        league_name = "League Test 2",
        description = "this is a test for a league",
        # start_date = date(2024, 9, 1),
        # end_date = date(2025, 2, 20),
        max_players_per_team = 16,
        max_teams = 12,
        max_bench = 6,
        admin_id = user4.id
    )

    # add league object to db
    db.session.add_all([
        league1, league2
    ])

    # commit db for league
    db.session.commit()

    # create team object
    team1 = Team(
        team_name = "Hardknocks1",
        # max_players_per_team = 16,
        # max_teams = 12,
        user_id = user1.id,
        league_id = league1.id
    )

    team2 = Team(
        team_name = "Hardknocks2",
        # max_players_per_team = 16,
        # max_teams = 12,
        user_id = user2.id,
        league_id = league1.id
    )

    team3 = Team(
        team_name = "Hardknocks3",
        # max_players_per_team = 16,
        # max_teams = 12,
        user_id = user3.id,
        league_id = league2.id
    )

    team4 = Team(
        team_name = "Hardknocks4",
        # max_teams = 12,
        # max_bench = 6,
        user_id = user4.id,
        league_id = league2.id
    )

    # add team object to db
    db.session.add_all([
        team1, team2, team3, team4
    ])

    # commit db for team
    db.session.commit()

    # log if seed succeeds
    print("Database has been seeded")

@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("tables dropped")

    # seed nfl tables and player tables from the get go?