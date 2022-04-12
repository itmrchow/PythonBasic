from common.ma import ma
from marshmallow import validate
from models.user import UserModel


class UserSchema(ma.Schema):
    class Meta:
        model = UserModel
    email = ma.Str(required=True)
    password = ma.Str(required=True, validate=[validate.Length(min=6, max=36)])
