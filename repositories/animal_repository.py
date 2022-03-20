from db.run_sql import run_sql
from repositories import vet_repository

def save(animal):
    sql = "INSERT INTO animals (name, dob, type, contact, notes) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [animal.name, animal.dob, animal.type, animal.contact, animal.notes]

    results = run_sql(sql, values)

    id = results[0]['id']
    animal.id = id

    return animal

