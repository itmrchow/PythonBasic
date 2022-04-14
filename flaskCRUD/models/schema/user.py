from common.ma import ma
from marshmallow import validate
from models.user import UserModel
from models.schema.post import PostSchemaResponse


class UserSchema(ma.Schema):
    class Meta:
        model = UserModel

    id = ma.Int()
    name = ma.Str()
    email = ma.Str(required=True)
    password = ma.Str(required=True, validate=[validate.Length(min=6, max=36)])
    posts = ma.List(ma.Nested(PostSchemaResponse))
