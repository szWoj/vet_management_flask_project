from models.animal import Animal
from models.vet import Vet

from repositories import vet_repository, animal_repository

animal_1 = Animal("Rex", "03-02-2021", "pudel", "07911-123456", "regular check-up")
animal_repository.save(animal_1)