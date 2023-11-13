# from app import app
import base64

from flask_bcrypt import check_password_hash
from src.models import User
from src.schema import UserSchema
from flask import request, Response, jsonify
import bcrypt
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash
from flask import Blueprint
import src.utils_db
from src.models import Session

session = Session()

user = Blueprint("user", __name__)

auth = HTTPBasicAuth()

users = {
    "john": generate_password_hash("hello"),
    "susan": generate_password_hash("bye")
}


@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username


@user.route("/login", methods=["POST"])
def login_user():
    data = request.get_json(force=True)
    src.schema.LoginSchema().load(data)

    message = data["username"] + ":" + data["password"]
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')

    try:
        user = src.utils_db.get_entry_by_username(User, UserSchema, data["username"])
    except:
        return "Не знайдено даного користувача", 404

    if user is not None and check_password_hash(user["password"], data["password"]):
        return base64_message
    else:
        return Response(status=404, response="[INVALID PASSWORD OR USERNAME]")


# from src.utils_db import create_entry


@user.route("/user", methods=["POST"])  # create new user
def create_user():
    user_data = UserSchema().load(request.get_json())
    if len(user_data["password"]) < 5:
        return Response(status=400, response="Password is too short")
    pwd = request.json.get('password', None)
    hashed_pwd = bcrypt.hashpw(pwd.encode("utf-8"), bcrypt.gensalt())
    user_data.update({"password": hashed_pwd, "userStatus": False})
    # return create_entry(User, UserSchema, **user_data).format(auth.current_user())
    return src.utils_db.create_entry(User, UserSchema, **user_data)


@user.route("/user", methods=["GET"])  # get all users
#@auth.login_required
def get_user():
    return src.utils_db.get_entries(User, UserSchema)


#
#
# @app.route("/user/<int:id>", methods=["GET"])  # get user by id
# def get_user_by_id(id):
#     return get_entry_by_id(User, UserSchema, id)
#
#
@user.route("/user/<string:username>", methods=["GET"])  # get user by username
def get_user_by_username(username):
     return src.utils_db.get_entry_by_username(User, UserSchema, username)
#
#
@user.route("/user/<int:id>", methods=["PUT"])  # update user by id
def update_user_by_id(id):
    user_data = UserSchema().load(request.get_json())
    return src.utils_db.update_entry_by_id(User, UserSchema, id, **user_data)


@user.route("/user/<string:username>", methods=["PUT"])  # update user by id
def update_user_by_username(username):
    user_data = UserSchema().load(request.get_json())
    print(user_data)
    if "password" in user_data.keys():
        if user_data["password"] == "":
            return Response(status=400, response="Пароль не може бути пусти")
        pwd = request.json.get('password', None)
        hashed_pwd = bcrypt.hashpw(pwd.encode("utf-8"), bcrypt.gensalt())
        user_data.update({"password": hashed_pwd})
    entry = session.query(User).filter_by(username=username).first()
    print(entry)
    if entry is None:
        return "error"
    for key, value in user_data.items():
        setattr(entry, key, value)
    if entry.username != username:
        return "error"
    session.commit()
    return jsonify(UserSchema().dump(entry))
    #return src.utils_db.update_entry_by_username(User, UserSchema, username, **user_data)


#
#
# @user.route("/user/<int:id>", methods=["DELETE"])  # delete user by id
# #@auth.login_required
# def delete_user_by_id(id):
#     return src.utils_db.delete_entry_by_id(User, UserSchema, id)

@user.route("/user/<string:username>", methods=["DELETE"])  # delete user by id
#@auth.login_required
def delete_user_by_username(username):
    print(username)
    return src.utils_db.delete_entry_by_username(User, UserSchema, username)
