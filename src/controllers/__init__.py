from controllers.users_controllers import users
from controllers.leagues_controllers import leagues
from controllers.auth_contollers import auth
from controllers.teams_controllers import teams
from controllers.players_controllers import players
from controllers.rosters_controllers import rosters

registered_controllers = (
    leagues,
    auth,
    users,
    teams,
    players,
    rosters,
)



# from flask import Blueprint

# # Define your blueprints without registering them
# users = Blueprint('users', __name__, url_prefix="/users")
# leagues = Blueprint('leagues', __name__, url_prefix="/leagues")
# auth = Blueprint('auth', __name__, url_prefix="/auth")
# teams = Blueprint('teams', __name__, url_prefix="/teams")
# players = Blueprint('players', __name__, url_prefix="/players")

# # Now you can import your controllers
# from controllers import users_controllers, leagues_controllers, auth_contollers, teams_controllers, players_controllers