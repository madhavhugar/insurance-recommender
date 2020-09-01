from typing import List
from collections import namedtuple

from api.views.insurance.types import (
    QuestionnareAnswers,
    RecommendationResponse,
)
from api.views.insurance.recommendation import (
    OccupationRecommendation,
    FamilyRecommendation,
    CityRecommendation,
    CountryRecommendation,
)

RecommenderType = namedtuple('Recommender', ['field', 'type'])


class Recommender:
    recommenders: List[RecommenderType] = [
        RecommenderType('occupation', OccupationRecommendation),
        RecommenderType('children', FamilyRecommendation),
        RecommenderType('address', CityRecommendation),
        RecommenderType('address', CountryRecommendation)
    ]

    def __init__(self, qa: QuestionnareAnswers):
        self.qa = qa

    def fetch_all(self) -> List[RecommendationResponse]:
        recommendations = []
        for recommender in self.recommenders:
            recommendation = recommender.type(self.qa[recommender.field]) \
                       .recommend()
            if recommendation:
                recommendations.append(recommendation)
        return recommendations
