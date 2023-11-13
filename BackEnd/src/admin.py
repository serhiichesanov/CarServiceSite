from app import app
from src.models import Admin
from src.schema import AdminSchema
from flask import request

from src.utils_db import (
    create_entry,
    get_entries,
    get_entry_by_id,
    update_entry_by_id,
    delete_entry_by_id,
)


@app.route("/admin", methods=["POST"])
def create_admin():
    admin_data = AdminSchema().load(request.get_json())

    return create_entry(Admin, AdminSchema, **admin_data)


@app.route("/admin", methods=["GET"])
def get_admin():
    return get_entries(Admin, AdminSchema)


@app.route("/admin/<int:id>", methods=["GET"])
def get_admin_by_id(id):
    return get_entry_by_id(Admin, AdminSchema, id)


@app.route("/admin/<int:id>", methods=["PUT"])
def update_admin_by_id(id):
    user_data = AdminSchema().load(request.get_json())
    return update_entry_by_id(Admin, AdminSchema, id, **user_data)


@app.route("/admin/<int:id>", methods=["DELETE"])
def delete_admin_by_id(id):
    return delete_entry_by_id(Admin, AdminSchema, id)
