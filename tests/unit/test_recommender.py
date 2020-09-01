from api.views.insurance.recommender import Recommender


def test_recommender():
    # should respond to user with valid recommendations
    questionnare_answers = {
        'email': 'test@testdomain.com',
        'num_children': 2,
        'children': True,
        'name': 'someonenew',
        'address': 'punkstr 42',
        'occupation': 'developer',
    }
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

    recommender = Recommender(questionnare_answers)
    assert recommender.fetch_all() == expected_recommendation
