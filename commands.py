from flask import Blueprint
from datetime import date

from main import db, bcrypt
from models import User, League, Team, Roster, Player

db_commands = Blueprint("db", __name__)

@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("tables created")

@db_commands.cli.command("seed")
def seed_db():

    users = User(
            username = "user1",
            first_name = "john",
            last_name = "doe",
            email = "user1@gmail.com",
            password = bcrypt.generate_password_hash("123456").decode("utf-8"),
        )

    # user2 = User(
    #     username = "hardcores2",
    #     first_name = "lewis",
    #     last_name = "hardie",
    #     email = "lewishardie2@gmail.com",
    #     password = bcrypt.generate_password_hash("123456").decode("utf-8"),
    # )

    # user3 = User(
    #     username = "hardcores3",
    #     first_name = "lewis",
    #     last_name = "hardie",
    #     email = "lewishardie3@gmail.com",
    #     password = bcrypt.generate_password_hash("123456").decode("utf-8"),
    # )

    # user4 = User(
    #     username = "hardcores4",
    #     first_name = "lewis",
    #     last_name = "hardie",
    #     email = "lewishardie4@gmail.com",
    #     password = bcrypt.generate_password_hash("123456").decode("utf-8"),
    # )

    # add all user objets to db
    db.session.add_all([users])

    # commit db for users
    db.session.commit()

    # create league object
    leagues = League(
            league_name = "League 1",
            description = "Description for League 1",
            # start_date = date(2024, 9, 1),
            # end_date = date(2025, 2, 20),
            max_players_per_team = 16,
            max_teams = 12,
            admin_id = users.id,
            # max_bench = 6,
        )

    # league2 = League(
    #     league_name = "League Test 2",
    #     description = "this is a test for a league",
    #     # start_date = date(2024, 9, 1),
    #     # end_date = date(2025, 2, 20),
    #     max_players_per_team = 16,
    #     max_teams = 12,
    #     max_bench = 6,
    #     admin_id = user4.id
    # )

    # add league object to db
    db.session.add_all([
        leagues,
    ])

    # commit db for league
    db.session.commit()

    # create team object
    teams = Team(
            team_name = "Team 1",
            user_id = users.id,
            league_id = leagues.id,
        )

    # team2 = Team(
    #     team_name = "Hardknocks2",
    #     # max_players_per_team = 16,
    #     # max_teams = 12,
    #     user_id = user2.id,
    #     league_id = league1.id
    # )

    # team3 = Team(
    #     team_name = "Hardknocks3",
    #     # max_players_per_team = 16,
    #     # max_teams = 12,
    #     user_id = user3.id,
    #     league_id = league2.id
    # )

    # team4 = Team(
    #     team_name = "Hardknocks4",
    #     # max_teams = 12,
    #     # max_bench = 6,
    #     user_id = user4.id,
    #     league_id = league2.id
    # )

    # add team object to db
    db.session.add_all([
        teams,
    ])

    # commit db for team
    db.session.commit()

    player = Player(
            first_name = "First Name 1",
            last_name = "Last Name",
            nfl_team = "Football Team",
            position = "QB",
            is_available = True,
            league_id = leagues.id,
        )
    player2 = Player(
        first_name = "First Name 2",
        last_name = "Last Name",
        nfl_team = "Football Team",
        position = "QB",
        is_available = True,
        league_id = leagues.id,
        )
    player3 = Player(
        first_name = "First Name 3",
        last_name = "Last Name",
        nfl_team = "Football Team",
        position = "QB",
        is_available = True,
        league_id = leagues.id,
        )
    player4 = Player(
        first_name = "First Name 4",
        last_name = "Last Name",
        nfl_team = "Football Team",
        position = "QB",
        is_available = True,
        league_id = leagues.id,
        )
    player5 = Player(
        first_name = "First Name 5",
        last_name = "Last Name",
        nfl_team = "Football Team",
        position = "QB",
        is_available = True,
        league_id = leagues.id,
        )
    player6 = Player(
        first_name = "First Name 6",
        last_name = "Last Name",
        nfl_team = "Football Team",
        position = "QB",
        is_available = True,
        league_id = leagues.id,
        )
    player7 = Player(
        first_name = "First Name 7",
        last_name = "Last Name",
        nfl_team = "Football Team",
        position = "QB",
        is_available = True,
        league_id = leagues.id,
        )
    player8 = Player(
        first_name = "First Name 8",
        last_name = "Last Name",
        nfl_team = "Football Team",
        position = "QB",
        is_available = True,
        league_id = leagues.id,
        )
    player9 = Player(
        first_name = "First Name 9",
        last_name = "Last Name",
        nfl_team = "Football Team",
        position = "QB",
        is_available = True,
        league_id = leagues.id,
        )
    player10 = Player(
        first_name = "First Name 10",
        last_name = "Last Name",
        nfl_team = "Football Team",
        position = "QB",
        is_available = True,
        league_id = leagues.id,
        )
    player11 = Player(
        first_name = "First Name 11",
        last_name = "Last Name",
        nfl_team = "Football Team",
        position = "QB",
        is_available = True,
        league_id = leagues.id,
        )

    # add team object to db
    db.session.add_all([
        player, player2, player3, player4, player5, player6, player7, player8, player9, player10, player11
    ])

    # commit db for team
    db.session.commit()

    rosters = Roster(
            roster_slot = "roster_slot 1",
            team_id = teams.id,
            player_id = player.id,
        )

    # add team object to db
    db.session.add_all([
        rosters,
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