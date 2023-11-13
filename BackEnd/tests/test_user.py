import json
import base64
from src import session
from src.models import User
import bcrypt

valid_creds = base64.b64encode(b'susan:bye').decode('utf-8')
invalid_creds = base64.b64encode(b'velya:bye').decode('utf-8')

data = {
    'userName': 'velya123',
    'firstName': 'Velya',
    'lastName': 'Snegozhukh',
    'email': 'camboenjoyer@liamg.com',
    'password': '1337',
    'phone': '8783'
}

invalid_data = {
    'usernomnomnomame': 'velya123',
    'firstName': 1,
    'lastName': 'Snegozhukh',
    'email': 'camboenjoyer@liamg.com',
    'password': '1337',
    'phone': '8783'
}

update_data = {
    'userName': 'vladimir_kovbasa',
    'firstName': 'Vladimir',
    'lastName': 'Kapcheniy',
    'email': 'ya_piyu_pepsi@liamg.com',
    'password': '228',
    'phone': '8783'
}


# get_users
def test_get_users_s(client):
    url = '/user'
    response = client.get(url, headers={'Authorization': 'Basic ' + valid_creds})

    assert response.status_code == 200


def test_get_users_unauthorized(client):
    url = '/user'
    response = client.get(url, headers={'Authorization': 'Basic ' + invalid_creds})

    assert response.status_code == 401


# create_user
def test_create_user_s(client):
    url = '/user'

    response = client.post(url, json=data)

    assert response.content_type == 'application/json'
    assert response.status_code == 200


def test_create_user_f(client):
    url = '/user'

    response = client.post(url, json=invalid_data)

    assert response.content_type != 'application/json'
    assert response.status_code == 500


# get_user_by_id
def test_get_user_s(client):
    user = session.query(User).order_by(User.id.desc()).first()

    url = "/user/" + str(user.id)
    response = client.get(url)
    response_data = response.get_data()

    print(response_data)
    response_data = json.loads(response_data)

    pwd = data["password"]
    pass_verify = bcrypt.checkpw(pwd.encode("utf-8"), response_data["password"].encode("utf-8"))

    assert response_data["userName"] == data["userName"]
    assert response_data["firstName"] == data["firstName"]
    assert response_data["lastName"] == data["lastName"]
    assert response_data["email"] == data["email"]
    assert pass_verify
    assert response_data["phone"] == data["phone"]
    assert isinstance(user, User)
    assert response.status_code == 200


def test_get_user_f(client):
    user = session.query(User).order_by(User.id.desc()).first()

    url = "/user/" + str(user.id + 1)
    response = client.get(url)

    assert isinstance(user, User)
    assert response.status_code == 404


# get_user_by_username
def test_get_user_uname_s(client):
    user = session.query(User).order_by(User.id.desc()).first()
    username = user.userName

    url = "/user/" + str(username)
    response = client.get(url)

    assert isinstance(user, User)
    assert response.status_code == 200


def test_get_user_uname_f(client):
    user = session.query(User).order_by(User.id.desc()).first()
    username = user.userName + "junk"

    url = "/user/" + str(username)
    response = client.get(url)

    assert isinstance(user, User)
    assert response.status_code == 404


# update_user_by_id
def test_update_user_by_id_s(client):
    user = session.query(User).order_by(User.id.desc()).first()
    url = "/user/" + str(user.id)

    response = client.put(url, json=update_data)

    assert isinstance(user, User)
    assert response.status_code == 200


def test_update_user_by_id_f(client):
    user = session.query(User).order_by(User.id.desc()).first()
    url = "/user/" + str(user.id)

    response = client.put(url, json=invalid_data)

    assert isinstance(user, User)
    assert response.status_code == 500


# delete_user
def test_delete_user_by_id_unauthorized(client):
    userid = session.query(User).order_by(User.id.desc()).first().id
    url = "/user/" + str(userid)
    response = client.delete(url, headers={'Authorization': 'Basic ' + invalid_creds})

    assert response.status_code == 401


def test_delete_user_by_id_no_creds(client):
    userid = session.query(User).order_by(User.id.desc()).first().id
    url = "/user/" + str(userid)
    response = client.delete(url)

    assert response.status_code == 401


def test_delete_user_by_id_s(client):
    userid = session.query(User).order_by(User.id.desc()).first().id
    url = "/user/" + str(userid)
    response = client.delete(url, headers={'Authorization': 'Basic ' + valid_creds})

    assert response.status_code == 200


