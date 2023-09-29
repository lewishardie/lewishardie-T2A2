from controllers.users_controllers import users
from controllers.league_controllers import leagues
from controllers.auth_contollers import auth


registered_controllers = (
    leagues,
    auth,
    users,
)