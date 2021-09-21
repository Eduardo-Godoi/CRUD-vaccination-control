from sqlalchemy import Column, Integer, String, DateTime
from app.configs.database import db
from dataclasses import dataclass



@dataclass
class Vaccination(db.Model):
    __tablename__ = 'vaccine_card'

    id: int
    cpf: str
    name: str
    first_shot_date: str
    second_shot_date: str
    vaccine_name: str
    health_unit_name: str

    id = Column(Integer, primary_key=True)
    cpf = Column(String(11), nullable=False)
    name = Column(String, nullable=False)
    first_shot_date = Column(DateTime)
    second_shot_date = Column(DateTime)
    vaccine_name = Column(String, nullable=False)
    health_unit_name = Column(String)
