from common.ma import ma
from common.db import db

from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate


from resources.user import User
from resources.user import Users
from resources.post import Post


from datetime import timezone, datetime


dt = datetime.now().replace(tzinfo=timezone.utc)
print("datetime:", dt)

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "mysql+pymysql://root:123456@127.0.0.1:3306/pytest"
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS "] = False
app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))

api = Api(app)

api.add_resource(User, "/user/<string:name>")
api.add_resource(Users, "/users")
api.add_resource(Post, "/post/<int:id>")
# api.add_resource(Post, "/post/")


db.init_app(app)
migrate = Migrate(app, db)
ma.init_app(app)

app.run(debug=True)
