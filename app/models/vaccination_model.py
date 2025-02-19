from sqlalchemy import Column, Integer, String, DateTime
from app.configs.database import db
from dataclasses import dataclass


@dataclass
class Vaccination(db.Model):
    __tablename__ = 'vaccine_card'

    cpf: str
    name: str
    first_shot_date: str
    second_shot_date: str
    vaccine_name: str
    health_unit_name: str

    cpf = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    first_shot_date = Column(DateTime)
    second_shot_date = Column(DateTime)
    vaccine_name = Column(String, nullable=False)
    health_unit_name = Column(String)
