from common.ma import ma
from common.db import db

from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate


from resources.user import User
from resources.user import Users


app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "mysql+pymysql://root:123456@127.0.0.1:3306/pytest"
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS "] = False
api = Api(app)

api.add_resource(User, "/user/<string:name>")
api.add_resource(Users, "/users")


db.init_app(app)
migrate = Migrate(app, db)
ma.init_app(app)

app.run(debug=True)
