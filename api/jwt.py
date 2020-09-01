from passlib.hash import pbkdf2_sha256
from typing import Optional, TypedDict

from api.models.user import User


def authenticate(username: str, password: str) -> Optional[User]:
    user = User.query.filter_by(username=username).first()
    if user and pbkdf2_sha256.verify(password, user.password):
        return user


AuthPayload = TypedDict(
    'Auth',
    {
        'iat': str,
        'exp': str,
        'nbf': str,
        'identity': str,
    },
)


def identity(payload: AuthPayload) -> Optional[User]:
    user_id = payload['identity']
    return User.query.get(user_id)
