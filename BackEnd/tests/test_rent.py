from src import session
from src.models import Car, User, Rent
from .test_user import test_create_user_s, test_delete_user_by_id_s
from .test_car import test_create_car_s, test_delete_car_by_id_s


def test_get_rents(client):
    response = client.get('/rent')

    assert response.content_type == 'application/json'
    assert response.status_code == 200


# create_rent
def test_create_rent_s(client):
    test_create_user_s(client)
    test_create_car_s(client)

    user = session.query(User).order_by(User.id.desc()).first()
    car = session.query(Car).order_by(Car.id.desc()).first()

    data = {
        'userId': user.id,
        'carId': car.id,
        'amountOfHours': 100,
        'dateTimeOfReservation': '2018-12-10T13:49:51.141Z',
        'status': 'approved'
    }

    response = client.post('/rent', json=data)

    assert response.content_type == 'application/json'
    assert response.status_code == 200


def test_create_rent_f(client):
    user = session.query(User).order_by(User.id.desc()).first()
    car = session.query(Car).order_by(Car.id.desc()).first()

    data = {
        'userIddimastrizhak': user.id,
        'carId': car.id,
        'amountOfHours': 100,
        'dateTimeOfReservation': '2018-12-10T13:49:51.141Z',
        'status': 'approved'
    }

    response = client.post('/rent', json=data)

    assert response.content_type != 'application/json'
    assert response.status_code == 500


# update_rent
def test_update_rend_f(client):
    user = session.query(User).order_by(User.id.desc()).first()
    rent = session.query(Rent).order_by(Rent.id.desc()).first()

    data = {
        'userId': user.id,
        'adminRights': 'dodik'
    }

    url = "/admin/" + str(rent.id)
    response = client.put(url, json=data)

    assert response.content_type != 'application/json'
    assert response.status_code == 500


def test_update_rent_s(client):
    user = session.query(User).order_by(User.id.desc()).first()
    car = session.query(Car).order_by(Car.id.desc()).first()
    rent = session.query(Rent).order_by(Rent.id.desc()).first()

    data = {
        'userId': user.id,
        'carId': car.id,
        'amountOfHours': 100,
        'dateTimeOfReservation': '2020-12-10T13:49:51.141Z',
        'status': 'approved'
    }

    url = "/rent/" + str(rent.id)
    response = client.put(url, json=data)

    assert response.content_type == 'application/json'
    assert response.status_code == 200


# get_rent_by_id
def test_get_rent_s(client):
    rent = session.query(Rent).order_by(Rent.id.desc()).first()

    url = "/rent/" + str(rent.id)
    response = client.get(url)

    assert isinstance(rent, Rent)
    assert response.status_code == 200


def test_get_rent_f(client):
    rent = session.query(Rent).order_by(Rent.id.desc()).first()

    url = "/rent/" + str(rent.id + 1)
    response = client.get(url)

    assert response.status_code == 404


# delete_rent
def test_delete_rent_f(client):
    rent = session.query(Rent).order_by(Rent.id.desc()).first()
    url = "/rent/" + str(rent.id + 1)
    response = client.delete(url)

    assert response.status_code == 404


def test_delete_rent_s(client):
    rent = session.query(Rent).order_by(Rent.id.desc()).first()
    url = "/rent/" + str(rent.id)
    response = client.delete(url)
    test_delete_user_by_id_s(client)
    test_delete_car_by_id_s(client)

    assert isinstance(rent, Rent)
    assert response.status_code == 200
