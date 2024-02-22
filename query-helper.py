from pony.orm import *
from datetime import datetime
import models


@db_session
def lookup_patient(birth_date):
    birth_date_obj = datetime.strptime(birth_date, '%Y-%m-%d').date()
    q = models.Patient.select(lambda p: p.date_of_birth == birth_date_obj)
    if q.count() > 1:
        raise Exception("Patient not found")

    q.show()