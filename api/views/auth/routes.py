import json

from schema import Schema, SchemaError
from flask import Blueprint, request
from passlib.hash import pbkdf2_sha256
from sqlalchemy.exc import IntegrityError

from api.models.base import db
from api.models.user import User
from api.views.auth.types import UserInfo, UserInfoType


auth = Blueprint('auth', __name__, url_prefix='/auth')


# POST => /signup
@auth.route('/signup', methods=['POST'])
def signup() -> (str, int):
    s: UserInfo = json.loads(request.data)
    try:
        Schema(UserInfoType).validate(s)
        password_hash = pbkdf2_sha256.hash(s.get('password'))
        user = User(**{
            'username': s.get('username'),
            'password': password_hash,
        })
        # TODO: abstract away adding user to db?
        db.session.add(user)
        db.session.commit()
        return 'Successful signup', 201
    except SchemaError:
        return 'Username or password must be string', 400
    except IntegrityError:
        return 'Username already exits', 409
