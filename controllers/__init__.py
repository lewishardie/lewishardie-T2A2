from controllers.users_controllers import users
from controllers.leagues_controllers import leagues
from controllers.auth_contollers import auth
from controllers.teams_controllers import teams


registered_controllers = (
    leagues,
    auth,
    users,
    teams,
)