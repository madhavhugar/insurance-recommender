from api.views.insurance.recommendation import (
    OccupationRecommendation,
    CityRecommendation,
    CountryRecommendation,
    FamilyRecommendation,
    )


def test_occupation_recommendation():
    # should recommend users who are developers
    occupation = OccupationRecommendation(occupation='developer')
    expected = {
                'id': 'sprint_estimate_insurance',
                'title': 'umm when estimates turn into promises',
                'status': 'RECOMMENDED',
                'provider': 'product owner',
    }
    assert occupation.recommend() == expected

    # should recommend users with other occupation
    occupation = OccupationRecommendation(occupation='designer')
    expected = {
            'id': 'job',
            'title': 'Job',
            'status': 'RECOMMENDED',
            'provider': 'abc',
    }
    assert occupation.recommend() == expected


def test_family_recommendation():
    # should recommend for users with children
    family = FamilyRecommendation(children=True)
    expected = {
        'id': 'life',
        'title': 'you know for... life',
        'status': 'RECOMMENDED',
        'provider': 'abc',
    }
    assert family.recommend() == expected

    # should recommend for users with no children
    family = FamilyRecommendation(children=False)
    expected = {
        'id': 'life',
        'title': 'you know for... life',
        'status': 'NOT_RECOMMENDED',
        'provider': 'abc',
    }
    assert family.recommend() == expected


def test_city_recommendation():
    # should recommend users when city is set
    city = CityRecommendation('apt 10, xyz street, berlin')
    expected = {
        'id': 'city',
        'title': 'based on the city you live',
        'status': 'RECOMMENDED',
        'provider': 'abc',
    }
    assert city.recommend() == expected

    # should not recommend users when address is unset
    city = CityRecommendation('')
    assert city.recommend() is None


def test_country_recommendation():
    # should recommend users when city is set
    country = CountryRecommendation('apt 10, xyz street, berlin')
    expected = {
        'id': 'country',
        'title': 'based on the country you live',
        'status': 'NEEDED',
        'provider': 'abc',
    }
    assert country.recommend() == expected

    # should not recommend users when address is unset
    country = CountryRecommendation('')
    assert country.recommend() is None
