from common.ma import ma
from models.user import PostModel


class PostSchema(ma.Schema):
    class Meta:
        model = PostModel

    title = ma.Str()
    content = ma.Str(required=True)


class PostSchemaResponse(ma.Schema):
    class Meta:
        model = PostModel

    title = ma.Str()
    content = ma.Str()
    posterId = ma.Int()
    create_date = ma.DateTime(format="iso")
    create_date_timestamp = ma.Int()

    def get_attribute(self, obj, key, default):

        if key == "create_date_timestamp":
            return obj.create_date.timestamp()
        else:
            return getattr(obj, key, default)
