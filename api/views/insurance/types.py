from typing import TypedDict, Literal


QuestionnareAnswersType = {
        'email': str,
        'name': str,
        'num_children': int,
        'address': str,
        'children': bool,
        'occupation': str,
}

QuestionnareAnswers = TypedDict(
    'QuestionnareAnswers',
    QuestionnareAnswersType,
)

NOT_RECOMMENDED = 'NOT_RECOMMENDED'
NEEDED = 'NEEDED'
RECOMMENDED = 'RECOMMENDED'
STATUS = Literal[RECOMMENDED, NEEDED, NOT_RECOMMENDED]

RecommendationResponse = TypedDict(
    'RecommendationResponse',
    {
        'id': str,
        'title': str,
        'status': STATUS,
        'provider': str,
    },
)
