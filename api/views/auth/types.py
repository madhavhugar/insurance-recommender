from typing import TypedDict


UserInfoType = {
        'username': str,
        'password': str,
}
UserInfo = TypedDict(
    'Signup',
    UserInfoType,
)
