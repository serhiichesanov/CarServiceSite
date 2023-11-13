from marshmallow import Schema, fields, validate


class UserSchema(Schema):
    id = fields.Integer()
    username = fields.String()
    firstName = fields.String()
    lastName = fields.String()
    email = fields.String()
    password = fields.String()
    phone = fields.String()
    userStatus = fields.Boolean()


class CarSchema(Schema):
    id = fields.Integer()
    carMark = fields.String()
    carSpeed = fields.Integer()
    carNumber = fields.Integer()


class RentSchema(Schema):
    id = fields.Integer()
    userId = fields.Integer()
    carId = fields.Integer()
    startRent = fields.DateTime()
    endRent = fields.DateTime()
    totalPrice = fields.Float()


class AdminSchema(Schema):
    id = fields.Integer()
    userId = fields.Integer()
    adminRights = fields.Str(validate=validate.OneOf(["employee", "managment", "owner"]))

class LoginSchema(Schema):
    username = fields.String()
    password = fields.String()
