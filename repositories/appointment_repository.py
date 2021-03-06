from db.run_sql import run_sql
from repositories import vet_repository
from repositories import animal_repository
from models.animal import Animal
from models.vet import Vet
from models.appointment import Appointment

def save(appointment):
    sql = "INSERT INTO appointments (date, time, vet_id, animal_id, checked_in) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [appointment.date, appointment.time, appointment.vet.id, appointment.animal.id, appointment.checked_in]

    results = run_sql(sql, values)

    id = results[0]['id']
    appointment.id = id

    return appointment

def select_all():
    appointments = []
    sql = "SELECT * FROM appointments"
    results = run_sql(sql)
    for row in results:
        vet=vet_repository.select(row['vet_id'])
        animal=animal_repository.select(row['animal_id'])
        appointment = Appointment(row['date'], row['time'],vet ,animal, row['checked_in'], row['id'])
        appointments.append(appointment)
    return appointments

def select(id):
    appointment = None
    sql = "SELECT * FROM appointments WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        vet=vet_repository.select(result['vet_id'])
        animal= animal_repository.select(result['animal_id'])
        appointment = Appointment(result["date"], result['time'],vet, animal, result["checked_in"],result["id"])
    return appointment


def check_in(appointment):
    sql = "UPDATE appointments SET checked_in = %s WHERE  id=%s"
    values = [appointment.checked_in, appointment.id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM appointments"
    run_sql(sql)