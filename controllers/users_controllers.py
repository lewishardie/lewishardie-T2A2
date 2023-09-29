from flask import Blueprint, jsonify, request

from main import db
from models.users import User
from schemas.users import user_schema, users_schema

# /user
users = Blueprint('user', __name__, url_prefix="/user")

# /users
@users.route("/", methods=["GET"])
def get_users():
    q = db.select(User)
    users = db.session.scalars(q)

    return jsonify(users_schema.dump(users))

# create users
# @users.route("/", methods=["POST"])
# def create_users():
#     user_json = user_schema.load(request.json)
#     user = User(**user_json)
#     db.session.add(user)
#     db.session.commit()

#     return jsonify(users_schema.dump(user))

# OPTIONS
#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------

# @tasks.route("/", methods=["POST"])
# def create_tasks():
#     task_json = task_schema.load(request.json)
#     task = Task(**task_json)
#     db.session.add(task)
#     db.session.commit()

#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------

# @pets.route("/", methods=["POST"])
# def create_pets():
#     pet = Pet(**pet_schema.load(request.json))

#     db.session.add(pet)
#     db.session.commit()

#     return jsonify(pet_schema.dump(pet))


#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
# project_fields = project_schema.load(request.json) # project_fields = the enterered values from the request json
#     # you can use keys assosiated with a form to use the data entered by a user
#     new_project = Project(
#         # ["title" is the key assigned to the first entry field]
#         title = project_fields["title"],
#         repository = project_fields["repository"],
#         description = project_fields["description"]
#     )
#     db.session.add(new_project)
#     db.session.commit()
#     return project_schema.dump(new_project)


#/users/<id> -> user with id
@users.route("/<int:user_id>", methods=["GET"])
def get_user(user_id: int):
    q = db.select(User).filter_by(id=user_id) #filter(User.id == id) is another option
    user = db.session.scalar(q)
    response = user_schema.dump(user)

    if response:
        return jsonify(response)

    return jsonify(message=f"User with id='{user_id}' not found")


# # /users/<id> -> Updating a user with id

# @users.route("<int:user_id>", methods=["PUT"])
# def update_users(user_id:id):
#     q = db.select(User).filter_by(id=user_id) #filter(User.id == id) is another option
#     user = db.session.scalar(q)
#     response = user_schema.dump(user)


#     if response:
#         user_json = user_schema.load(request.json)
#         user.email = user_json["email"]
#         user = User(user_json)
#         db.session.commit()
#         return jsonify(users_schema.dump(user))

#     return jsonify(message=f"User with id='{user_id}' not found")