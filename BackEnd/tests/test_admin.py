import pytest
from src import session
from src.models import User, Admin
from .test_user import test_create_user_s
from .test_user import test_delete_user_by_id_s
from .test_utils import get_last_entry


@pytest.fixture()
def user_fixture(client):
    test_create_user_s(client)
    user = get_last_entry(session, User)
    yield user
    test_delete_user_by_id_s(client)


@pytest.fixture()
def user_delete_fixture(client):
    test_create_user_s(client)
    user = get_last_entry(session, User)
    yield user


def test_get_admins(client):
    response = client.get('/admin')

    assert response.status_code == 200


# create_admin
def test_create_admin_s(client, user_fixture):
    test_create_user_s(client)
    # user = get_last_entry(session, User)
    user = user_fixture

    data = {
        'userId': user.id,
        'adminRights': 'owner'
    }

    url = '/admin'
    response = client.post(url, json=data)

    assert response.content_type == 'application/json'
    assert response.status_code == 200


def test_create_admin_f(client, user_fixture):
    # user = get_last_entry(session, User)
    user = user_fixture

    data = {
        'userIdaboba': user.id,
        'adminRights': 'owner'
    }

    url = '/admin'
    response = client.post(url, json=data)

    assert response.content_type != 'application/json'
    assert response.status_code == 500


# update_admin_by_id
def test_update_admin_f(client, user_fixture):
    # user = get_last_entry(session, User)
    user = user_fixture
    admin = get_last_entry(session, Admin)

    data = {
        'userId': user.id,
        'adminRights': 'dodik'
    }

    url = "/admin/" + str(admin.id)
    response = client.put(url, json=data)

    assert response.content_type != 'application/json'
    assert response.status_code == 500


def test_update_admin_s(client, user_fixture):
    # user = get_last_entry(session, User)
    user = user_fixture
    admin = get_last_entry(session, Admin)

    data = {
        'userId': user.id,
        'adminRights': 'employee'
    }

    url = "/admin/" + str(admin.id)
    response = client.put(url, json=data)

    assert response.content_type == 'application/json'
    assert response.status_code == 200


# get_admin_by_id
def test_get_admin_s(client, user_fixture):
    user = user_fixture

    data = {
        'userId': user.id,
        'adminRights': 'owner'
    }

    url = '/admin'
    response = client.post(url, json=data)

    admin = get_last_entry(session, Admin)

    url = "/admin/" + str(admin.id)
    response = client.get(url)

    assert isinstance(admin, Admin)
    assert response.status_code == 200


def test_get_admin_f(client, user_fixture):
    user = user_fixture

    data = {
        'userId': user.id,
        'adminRights': 'owner'
    }

    url = '/admin'
    response = client.post(url, json=data)

    admin = get_last_entry(session, Admin)

    url = "/admin/" + str(admin.id + 1)
    response = client.get(url)

    assert response.status_code == 404


# delete_admin_by_id
def test_delete_admin_f(client, user_fixture):
    user = user_fixture
    data = {
        'userId': user.id,
        'adminRights': 'owner'
    }

    url = '/admin'
    response = client.post(url, json=data)

    admin = get_last_entry(session, Admin)
    url = "/admin/" + str(admin.id + 1)
    response = client.delete(url)

    assert response.status_code == 404


def test_delete_admin_s(client, user_delete_fixture):
    user = user_delete_fixture
    data = {
        'userId': user.id,
        'adminRights': 'owner'
    }

    url = '/admin'
    response = client.post(url, json=data)

    admin = get_last_entry(session, Admin)
    url = "/admin/" + str(admin.id)
    response = client.delete(url)
    test_delete_user_by_id_s(client)

    assert isinstance(admin, Admin)
    assert response.status_code == 200
