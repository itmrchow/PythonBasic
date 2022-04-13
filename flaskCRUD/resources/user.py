from flask import request
from flask_restful import Resource
from models.schema.user import UserSchema
from models.user import UserModel


user_schema = UserSchema(many=False)
users_schema = UserSchema(many=True)


class User(Resource):
    def get(self, name):
        user = UserModel.get_user(name)
        if not user:
            return {"message": "username not exist!"}, 403
        return user_schema.dump(user)

    def post(self, name):
        result = user_schema.load(request.json)
        user = UserModel(name, result["email"], result["password"])
        user.add_user()

        return {"message": "Insert user success", "user": user_schema.dump(user)}

    def put(self, name):
        result = user_schema.load(request.json)
        user = UserModel.get_user(name)

        if not user:
            return {"message": "username not exist!"}, 403

        user.name = name
        user.email = result["email"]
        user.password = result["password"]
        user.update_user()
        return {"message": "Update user success", "user": user_schema.dump(user)}

    def delete(self, name):
        UserModel.delete_user(name)
        return {"message": "Delete done"}

    # def patch(self, name):
    #     find = [item for item in users if item['name'] == name]
    #     if len(find) == 0:
    #         return {
    #             'message': 'username not exist!'
    #         }, 403

    #     user = users[0]
    #     arg = self.parser_patch.parse_args()

    #     for key, value in arg.items():
    #         if value is None:
    #             continue
    #         user[key] = value

    #     return {
    #         'message': 'Patch user success',
    #         'user': user
    #     }


class Users(Resource):
    def get(self):
        users = UserModel.get_all_users()
        dump_users = users_schema.dump(users)
        return {"message": "", "users": dump_users}
