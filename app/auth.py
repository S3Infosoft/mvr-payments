from app.model import User
from flask_restful import Resource, reqparse
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_refresh_token_required,
    get_jwt_identity,
    jwt_required,
    fresh_jwt_required
)

class UserLogin(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument(
        'email',
        type = str,
        required = True
    )

    parser.add_argument(
        'password',
        type = str,
        required = True
    )

    def post(self):

        data = self.parser.parse_args()
        user = User.query.get(data['email'])

        if user and user.verify(data['password']):
            access_token = create_access_token(identity = user.email, fresh = True)
            refresh_token = create_refresh_token(user.email)

            return {
                'access_token': access_token,
                'refresh_token': refresh_token
            }, 200

        return {'message':'invalid credentials'}, 401

class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        cur_usr = get_jwt_identity()
        new_token = create_access_token(identity = cur_usr, fresh= False)
        return {'access_token': new_token}, 200