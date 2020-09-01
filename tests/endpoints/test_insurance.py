import json

from flask import Flask

from api.models.base import db
from api.models.questionnare import Questionnare


def test_insurance_questionnare(client: Flask):
    user_data = {
        'username': 'testquestionnare',
        'password': 'test123',
    }
    client.post("/auth/signup", data=json.dumps(user_data))
    login_response = client.post('/auth/login', json=user_data)
    access_token = json.loads(login_response.data)['access_token']
    headers = {
        'Authorization': f'JWT {access_token}',
    }

    # should create a record when user with valid jwt submits a questionnare
    questionnare_answers = {
        'email': 'test@testdomain.com',
        'num_children': 2,
        'children': True,
        'name': 'someonenew',
        'address': 'punkstr 42',
        'occupation': 'informatik engineer'
    }
    response = client.post(
        '/insurance/questionnare',
        headers=headers,
        json=questionnare_answers,
    )
    emails = db.session.query(Questionnare.email).all()
    assert len(emails) == 1
    assert emails[0][0] == 'test@testdomain.com'
    assert response.status_code == 201
    assert response.data == b'Thank you for submitting your answers'

    # should return a schema error (HTTP 400) on invalid questionnare
    invalid_questionnare_answers = {
        'num_children': 2,
        'children': True,
        'name': 'someonenew',
        'address': 'punkstr 42',
        'occupation': 'informatik engineer'
    }
    response = client.post(
        '/insurance/questionnare',
        headers=headers,
        json=invalid_questionnare_answers,
    )
    assert response.status_code == 400
    assert response.data == b'Invalid questionnare input'

    # should not allow user with invalid jwt to submit questionnare
    header_with_invalid_jwt = {
        'Authorization': 'JWT invalid_jwt_token',
    }
    questionnare_answers = {
        'email': 'test@testdomain.com',
        'num_children': 2,
        'children': True,
        'name': 'someonenew',
        'address': 'punkstr 42',
        'occupation': 'informatik engineer'
    }
    response = client.post(
        '/insurance/questionnare',
        headers=header_with_invalid_jwt,
        json=questionnare_answers,
    )
    assert response.status_code == 401

    # # should not create a record when user has already submitted questionnare
    # questionnare_answers = {
    #     'email': 'test@testdomain.com',
    #     'num_children': 2,
    #     'children': True,
    #     'name': 'someonenew',
    #     'address': 'punkstr 42',
    #     'occupation': 'informatik engineer'
    # }
    # response = client.post(
    #     '/insurance/questionnare',
    #     headers=headers,
    #     json=questionnare_answers,
    # )
    # assert response.status_code == 200
    # assert response.data == b'We have already received your answers'


def test_insurance_recommendation(client: Flask):
    user_data = {
        'username': 'testrecommendation',
        'password': 'test123',
    }
    client.post("/auth/signup", data=json.dumps(user_data))
    login_response = client.post('/auth/login', json=user_data)
    access_token = json.loads(login_response.data)['access_token']
    headers = {
        'Authorization': f'JWT {access_token}',
    }
    recommendation_input = {
        'email': 'test@testdomain.com',
        'num_children': 2,
        'children': True,
        'name': 'someonenew',
        'address': 'punkstr 42',
        'occupation': 'software developer',
    }

    # should return recommendation when user with valid jwt
    # submits recommendation input
    response = client.post(
        '/insurance/recommendation',
        headers=headers,
        json=recommendation_input,
    )
    expected_recommendation = [
        {
            "id": "sprint_estimate_insurance",
            "title": "umm when estimates turn into promises",
            "status": "RECOMMENDED",
            "provider": "product owner"
        },
        {
            "id": "life",
            "title": "you know for... life",
            "status": "RECOMMENDED",
            "provider": "abc"
        },
        {
            "id": "city",
            "title": "based on the city you live",
            "status": "RECOMMENDED",
            "provider": "abc"
        },
        {
            "id": "country",
            "title": "based on the country you live",
            "status": "NEEDED",
            "provider": "abc"
        }
    ]
    assert response.status_code == 202
    assert json.loads(response.data) == expected_recommendation

    # should return a schema error (HTTP 400) on invalid recommendation input
    invalid_recommendation_input = {
        'num_children': 2,
        'children': True,
        'address': 'punkstr 42',
        'occupation': 'software developer',
    }
    response = client.post(
        '/insurance/recommendation',
        headers=headers,
        json=invalid_recommendation_input,
    )
    assert response.status_code == 400

    # should not allow user with invalid jwt to submit questionnare
    header_with_invalid_jwt = {
        'Authorization': 'JWT invalid_jwt_token',
    }
    response = client.post(
        '/insurance/questionnare',
        headers=header_with_invalid_jwt,
        json=recommendation_input,
    )
    assert response.status_code == 401
