from datetime import date
from datetime import datetime
from pony.orm import *


db = Database()


class Doctor(db.Entity):
    id = PrimaryKey(int, auto=True)
    last_name = Required(str)
    first_name = Required(str)
    patronymic = Optional(str)
    fee_per_visit = Required(float)
    visits = Set('Visit')


class Visit(db.Entity):
    id = PrimaryKey(int, auto=True)
    doctor = Required(Doctor)
    patient = Required('Patient')
    weight = Optional(float)
    height = Optional(float)
    conclusion = Required(str, default="Патологии не выявлено.")
    timestamp = Required(datetime, default=datetime.now())


class Patient(db.Entity):
    id = PrimaryKey(int, auto=True)
    last_name = Required(str)
    first_name = Required(str)
    patronymic = Optional(str)
    gender = Optional(str, 1)
    date_of_birth = Required(date)
    visits = Set(Visit)


def get_entity_names():
    entity_names = list()

    for entity_name, entity_cls in db.entities.items():
        entity_names.append(entity_name)

    return entity_names


@db_session
def populate_sample_data(cls, data):
    if select(x for x in cls).count() > 0:
        print(f'Таблица {cls} уже содержит данные.')
        return

    for item in data:
        cls(**item)
