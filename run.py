from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_jwt_extended import JWTManager
import os

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DB")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
app.config['SECRET_KEY'] = 'some-secret-string'


db = SQLAlchemy(app)


@app.before_first_request
def create_tables():
    db.create_all()


app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY")
jwt = JWTManager(app)

app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return model.RevokedTokenModel.is_jti_blacklisted(jti)


from models import model
from resources import resource


api.add_resource(resource.UserRegistration, '/registration')
api.add_resource(resource.UserLogin, '/login')
api.add_resource(resource.UserLogoutAccess, '/logout/access')
api.add_resource(resource.UserLogoutRefresh, '/logout/refresh')
api.add_resource(resource.TokenRefresh, '/token/refresh')
api.add_resource(resource.Base2, '/base2')

parser = reqparse.RequestParser()
parser.add_argument('username', help='This field cannot be blank', required=True)
parser.add_argument('password', help='This field cannot be blank', required=True)


class UserRegistration(Resource):
    def post(self):
        data = parser.parse_args()
        return data


class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        return data
