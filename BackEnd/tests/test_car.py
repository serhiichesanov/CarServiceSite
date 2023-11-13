from src import session
from src.models import Car


data = {
    'carMark': 'Beamer',
    'carSpeed': 100,
    'carNumber': 1488
}

update_data = {
    'carMark': "'Cedes",
    'carSpeed': 90,
    'carNumber': 1337
}

invalid_data = {
    'field': 1,
    'carSpeed': 'junk',
    'carNumber': 1488
}


def test_get_cars(client):
    response = client.get('/car')

    assert response.content_type == 'application/json'
    assert response.status_code == 200


# create_car
def test_create_car_s(client):
    url = '/car'

    response = client.post(url, json=data)

    assert response.content_type == 'application/json'
    assert response.status_code == 200


def test_create_car_f(client):
    url = '/car'

    response = client.post(url, json=invalid_data)

    assert response.content_type != 'application/json'
    assert response.status_code == 500


# get_car_by_id
def test_get_car_s(client):
    car = session.query(Car).order_by(Car.id.desc()).first()

    url = "/car/" + str(car.id)
    response = client.get(url)

    assert isinstance(car, Car)
    assert response.status_code == 200


def test_get_car_f(client):
    car = session.query(Car).order_by(Car.id.desc()).first()
    carid = car.id + 1

    url = "/car/" + str(carid)
    response = client.get(url)

    assert isinstance(car, Car)
    assert response.status_code == 404


# update_car_by_id
def test_update_car_by_id_s(client):
    car = session.query(Car).order_by(Car.id.desc()).first()
    url = "/car/" + str(car.id)

    response = client.put(url, json=update_data)

    assert isinstance(car, Car)
    assert response.status_code == 200


def test_update_car_by_id_f(client):
    car = session.query(Car).order_by(Car.id.desc()).first()
    url = "/car/" + str(car.id)

    response = client.put(url, json=invalid_data)

    assert isinstance(car, Car)
    assert response.status_code == 500


# delete_car
def test_delete_car_by_id_s(client):
    carid = session.query(Car).order_by(Car.id.desc()).first().id
    url = "/car/" + str(carid)
    response = client.delete(url)

    assert response.status_code == 200


def test_delete_car_by_id_f(client):
    test_create_car_s(client)
    carid = session.query(Car).order_by(Car.id.desc()).first().id + 1
    url = "/car/" + str(carid)
    response = client.delete(url)

    test_delete_car_by_id_s(client)

    assert response.status_code == 404
