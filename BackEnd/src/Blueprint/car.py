#from app import app
from src.models import Car
from src.schema import CarSchema
from flask import request
from flask import Blueprint

import src.utils_db

car = Blueprint("car", __name__)

@car.route("/car", methods=["POST"])
def create_car():
    rent_data = CarSchema().load(request.get_json())

    return src.utils_db.create_entry(Car, CarSchema, **rent_data)


@car.route("/car", methods=["GET"])
def get_car():
    return src.utils_db.get_entries(Car, CarSchema)


@car.route("/car/<int:id>", methods=["GET"])
def get_car_by_id(id):
    return src.utils_db.get_entry_by_id(Car, CarSchema, id)


@car.route("/car/<int:id>", methods=["PUT"])
def update_car_by_id(id):
    user_data = CarSchema().load(request.get_json())
    return src.utils_db.update_entry_by_id(Car, CarSchema, id, **user_data)


@car.route("/car/<int:id>", methods=["DELETE"])
def delete_car_by_id(id):
    return src.utils_db.delete_entry_by_id(Car, CarSchema, id)
