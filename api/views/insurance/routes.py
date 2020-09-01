import json

from flask import Blueprint, request
from flask import current_app as app
from flask_jwt import jwt_required
from schema import Schema, SchemaError
from sqlalchemy.exc import IntegrityError


from api.models.base import db
from api.models.questionnare import Questionnare
from api.views.insurance.recommender import Recommender
from api.views.insurance.types import (
    QuestionnareAnswers,
    QuestionnareAnswersType,
)


insurance = Blueprint('insurance', __name__, url_prefix='/insurance')


# POST => /questionnare
@insurance.route('/questionnare', methods=['POST'])
@jwt_required()
def questionnare() -> (str, int):
    qa: QuestionnareAnswers = json.loads(request.data)
    app.logger.info(f'POST => /questionnare {qa}')
    try:
        Schema(QuestionnareAnswersType).validate(qa)
        questionnare = Questionnare(**qa)
        db.session.add(questionnare)
        db.session.commit()
        return 'Thank you for submitting your answers', 201
    except IntegrityError:
        app.logger.error('POST => /questionnare: integrity error')
        return 'We have already received your answers', 200
    except SchemaError:
        app.logger.error('POST => /questionnare: schema error')
        return 'Invalid questionnare input', 400


# POST => /recommendation
@insurance.route('/recommendation', methods=['POST'])
@jwt_required()
def recommendation() -> (str, int):
    qa: QuestionnareAnswers = json.loads(request.data)
    app.logger.info(f'POST => /recommendation {qa}')
    try:
        Schema(QuestionnareAnswersType).validate(qa)
        recommendations = Recommender(qa).fetch_all()
        return json.dumps(recommendations), 202
    except SchemaError:
        app.logger.error('POST => /recommendation: schema error')
        return 'Invalid recommendation input', 400
