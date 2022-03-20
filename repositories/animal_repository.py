from db.run_sql import run_sql
from repositories import vet_repository
from models.animal import Animal

def save(animal):
    sql = "INSERT INTO animals (name, dob, type, contact, notes) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [animal.name, animal.dob, animal.type, animal.contact, animal.notes]

    results = run_sql(sql, values)

    id = results[0]['id']
    animal.id = id

    return animal

def select(id):
    animal = None
    sql = "SELECT * FROM animals WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        animal = Animal(result["name"], result['dob'], result['type'], result['contact'], result['notes'], id)
    return animal