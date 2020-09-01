from typing import Optional

from api.views.insurance.types import (
    NEEDED,
    RECOMMENDED,
    NOT_RECOMMENDED,
    RecommendationResponse,
)


class Recommendation:
    def recommend(self) -> Optional[RecommendationResponse]:
        raise 'recommend not implemented'


class OccupationRecommendation(Recommendation):
    def __init__(self, occupation: str):
        self.occupation = occupation

    def recommend(self) -> Optional[RecommendationResponse]:
        if not self.occupation:
            return None
        if self.occupation.lower().find('developer') > -1:
            return {
                'id': 'sprint_estimate_insurance',
                'title': 'umm when estimates turn into promises',
                'status': RECOMMENDED,
                'provider': 'product owner',
            }
        return {
            'id': 'job',
            'title': 'Job',
            'status': RECOMMENDED,
            'provider': 'abc',
        }


class FamilyRecommendation(Recommendation):
    def __init__(self, children: bool):
        self.children = children

    def recommend(self) -> Optional[RecommendationResponse]:
        if self.children:
            return {
                'id': 'life',
                'title': 'you know for... life',
                'status': RECOMMENDED,
                'provider': 'abc',
            }
        return {
            'id': 'life',
            'title': 'you know for... life',
            'status': NOT_RECOMMENDED,
            'provider': 'abc',
        }


class CityRecommendation(Recommendation):
    def __init__(self, address: str):
        self.address = address

    def recommend(self) -> Optional[RecommendationResponse]:
        if not self.address:
            return None
        return {
            'id': 'city',
            'title': 'based on the city you live',
            'status': RECOMMENDED,
            'provider': 'abc',
        }


class CountryRecommendation(Recommendation):
    def __init__(self, address: str):
        self.address = address

    def recommend(self) -> Optional[RecommendationResponse]:
        if not self.address:
            return None
        return {
            'id': 'country',
            'title': 'based on the country you live',
            'status': NEEDED,
            'provider': 'abc',
        }
