import json

from flask import Flask


def test_auth_login(client: Flask):
    # should return a jwt for a valid user
    data = {
        'username': 'testlogin',
        'password': 'test123',
    }
    client.post("/auth/signup", data=json.dumps(data))
    response = client.post('/auth/login', json=data)
    assert response.status_code == 200
    # assert None == 1
    assert json.loads(response.data)['access_token'] is not None


def test_auth_signup(client: Flask):
    # should return 400 when username or password is invalid
    invalid_data = {
        'username': 123456,
        'password': 'test123',
    }
    response = client.post('/auth/signup', data=json.dumps(invalid_data))
    assert response.status_code == 400
    assert response.data == b'Username or password must be string'

    invalid_data = {
        'username': 'test',
        'password': 1234567,
    }
    response = client.post('/auth/signup', data=json.dumps(invalid_data))
    assert response.status_code == 400
    assert response.data == b'Username or password must be string'

    # should return 201 when user signup is successful
    data = {
        'username': 'test',
        'password': 'test123',
    }
    response = client.post('/auth/signup', data=json.dumps(data))
    assert response.status_code == 201
    assert response.data == b'Successful signup'

    # # should return 409 when existing user tries to signup
    # response = client.post('/auth/signup', data=json.dumps(data))
    # assert response.status_code == 409
    # assert response.data == b'Username already exits'
