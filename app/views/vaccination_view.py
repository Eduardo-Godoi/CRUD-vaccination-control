import datetime

from app.models.vaccination_model import Vaccination
from flask import Blueprint, current_app, jsonify, request
from sqlalchemy.exc import IntegrityError

bp = Blueprint('vaccination', __name__, url_prefix='/vaccination')


@bp.post('')
def create():
    try:
        data = request.get_json()

        if len(data['cpf']) != 11 or not data['cpf'].isnumeric():
            return {'msg': 'Envie um CPF válido'}, 400

        new_vaccine = Vaccination(
            cpf=data["cpf"],
            name=data['name'],
            first_shot_date=datetime.date.today(),
            second_shot_date=datetime.date.today() + datetime.timedelta(+90),
            vaccine_name=data['vaccine_name'],
            health_unit_name=data['health_unit_name']
        )

        session = current_app.db.session
        session.add(new_vaccine)
        session.commit()

        return jsonify(new_vaccine), 201
    except IntegrityError:
        return {'msg': 'O CPF enviado já foi cadastrado'}, 409


@bp.get('')
def get_all():
    query = Vaccination.query.all()
    return jsonify(query), 200
