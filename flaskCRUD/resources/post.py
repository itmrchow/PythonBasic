import json
from flask import request
from flask_restful import Resource

from models.schema.post import PostSchema
from models.schema.post import PostSchemaResponse
from models.post import PostModel
from models.user import UserModel


post_schema = PostSchema(many=False)
post_schema_response = PostSchemaResponse(many=False)
post_schema_responses = PostSchemaResponse(many=False)


class Post(Resource):
    def post(self):
        result = post_schema.load(request.json)
        name = result["name"]
        # search user exist
        user = UserModel.get_user(name)
        if not user:
            return {"message": "username not exist!"}

        post = PostModel(
            title=result["title"], content=result["content"], poster_id=user.id
        )

        post.add_post()

        return {
            "message": "Insert {} post success".format(name),
            "post": post_schema_response.dump(post),
        }

    def get(self, id):
        print(request)
        post = PostModel.get_post(id)
        if not post:
            return {"message": "id not exist!"}, 403
        response = post_schema_response.dump(post)
        return response


class Posts(Resource):
    def get(self):
        posts = PostModel.get_all_posts()
        dump_posts = post_schema_response.dump(posts)
        return {"message": "", "users": dump_posts}
