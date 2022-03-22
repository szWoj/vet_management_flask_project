from db.run_sql import run_sql
from repositories import vet_repository
from repositories import animal_repository
from models.animal import Animal
from models.vet import Vet
from models.appointment import Appointment

def save(appointment):
    sql = "INSERT INTO appointments (date, time, vet_id, animal_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [appointment.date, appointment.time, appointment.vet.id, appointment.animal.id]

    results = run_sql(sql, values)

    id = results[0]['id']
    appointment.id = id

    return appointment