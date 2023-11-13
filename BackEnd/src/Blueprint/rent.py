#from app import app
from _datetime import datetime, date

from src.models import Rent
from src.schema import RentSchema
from flask import request, Blueprint, jsonify, Response
from src.models import Session, Rent, Car
import src.utils_db

rent = Blueprint("rent", __name__)

@rent.route("/rent", methods=["POST"])
def create_rent():
    data = request.get_json()
    try:
        car_id = int(request.json.get('carId', None))
    except:
        return Response(status=403, response="ID машини введено не корректно")
    cars = Session.query(Car).all()
    flag = False
    for car in cars:
        if car.id == car_id:
            flag = True
            break
    if not flag:
        return Response(status=403, response="Такої машини не існує")
    try:
        start = datetime.strptime(data["startRent"], '%Y-%m-%d %H:%M:%S')
        end = datetime.strptime(data["endRent"], '%Y-%m-%d %H:%M:%S')
    except:
        return Response(status=403, response="Заданий час некоректний")


    if start > end:
        return Response(status=403, response="Заданий час некоректний")

    rents = Session.query(Rent).all()

    delta = end - start

    today = datetime.combine(date.today(), datetime.min.time())
    if start < today or end < today:
        return Response(status=403, response="Введене дата не може бути у минулому")

    if delta.days > 7:
        return Response(status=403, response="Найбільший час аренди: 7 днів")
    if delta.total_seconds()/3600 < 1:
        return Response(status=403, response="Найменший час аренди: 1 година")
    for rent in rents:
        if rent.carId != car_id:
            continue

        db_start = rent.startRent
        db_end = rent.endRent

        if start <= db_start and db_end <= end:
            return  Response(status=403, response="Даний час вже зайнятий")
        elif start > db_start and db_end > end:
            return Response(status=403, response="Даний час вже зайнятий")
        elif start < db_start and end > db_start:
            return Response(status=403, response="Даний час вже зайнятий")
        elif start < db_end and end > db_end:
            return Response(status=403, response="Даний час вже зайнятий")
    car_price = Session.query(Car).filter_by(id=car_id).first()
    print(car_price.carNumber)
    data.update({"totalPrice": car_price.carNumber * delta.total_seconds()/3600})

    rent_data = RentSchema().load(data)

    return src.utils_db.create_entry(Rent, RentSchema, **rent_data)


@rent.route("/rent", methods=["GET"])
def get_rent():
    return src.utils_db.get_entries(Rent, RentSchema)


@rent.route("/rent/<int:id>", methods=["GET"])
def get_rent_by_id(id):
    return src.utils_db.get_entry_by_id(Rent, RentSchema, id)


@rent.route("/rent/<int:id>", methods=["PUT"])
def update_rent_by_id(id):
    user_data = RentSchema().load(request.get_json())
    return src.utils_db.update_entry_by_id(Rent, RentSchema, id, **user_data)


@rent.route("/rent/<int:id>", methods=["DELETE"])
def delete_rent_by_id(id):
    return src.utils_db.delete_entry_by_id(Rent, RentSchema, id)
