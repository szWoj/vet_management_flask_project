from models.animal import Animal
from models.vet import Vet

from repositories import vet_repository, animal_repository

# animal_1 = Animal("Rex", "03-02-2021", "pudel", "07911-123456", "regular check-up")
# animal_repository.save(animal_1)

# print(animal_repository.select(animal_1.id).__dict__)



animal_repository.delete(2)

all_animals = animal_repository.select_all()
for animal in all_animals:
    print(animal.__dict__)