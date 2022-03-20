
from db.run_sql import run_sql
from repositories import vet_repository
from models.animal import Animal

def save(animal):
    sql = "INSERT INTO animals (name, vet_id, dob, type, contact, notes) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [animal.name, animal.vet.id, animal.dob, animal.type, animal.contact, animal.notes]

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
        #this will be added later to get vet vet=vet_repository.select(['vet_id])
        animal = Animal(result["name"], result['dob'], result['type'], result['contact'], result['notes'], id)
    return animal

def select_all():
    animals = []
    sql = "SELECT * FROM animals"
    results = run_sql(sql)
    for row in results:
        animal = Animal(row['name'], row['dob'], row['type'], row['contact'], row['notes'], row['id'])
        animals.append(animal)
    return animals

def delete(id):
    sql = "DELETE FROM animals WHERE id = %s"
    values=[id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM animals"
    run_sql(sql)

def update(animal):
    sql = "UPDATE animals SET (name, vet_id, dob, type, contact, notes, ) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [animal.name, animal.vet.id, animal.dob, animal.type, animal.contact, animal.notes, animal.id]
    run_sql(sql, values)