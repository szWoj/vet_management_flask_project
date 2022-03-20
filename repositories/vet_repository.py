from db.run_sql import run_sql

from models.animal import Animal
from models.vet import Vet
from repositories import animal_repository

def save(vet):
    sql = "INSERT INTO vets (name, contact, status) VALUES (%s, %s, %s) RETURNING *"
    values = [vet.name, vet.contact, vet.status]

    results = run_sql(sql, values)

    id = results[0]['id']
    vet.id = id

    return vet

def select(id):
    vet = None
    sql = "SELECT * FROM vets WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        
        vet = Vet(result["name"], result['contact'], result['status'], id)
    return vet