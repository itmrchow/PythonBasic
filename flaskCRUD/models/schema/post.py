from common.ma import ma
from models.user import PostModel


class PostSchema(ma.Schema):
    class Meta:
        model = PostModel

    title = ma.Str()
    content = ma.Str(required=True)
    poster_id = ma.Int(required=True)
