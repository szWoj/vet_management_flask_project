from models.animal import Animal
from models.vet import Vet

from repositories import vet_repository, animal_repository

# animal_1 = Animal("Meg", "03-02-2021", "pudel", "07911-123456", "regular check-up")
# animal_repository.save(animal_1)

# print(animal_repository.select(animal_1.id).__dict__)

# animal_repository.delete(2)
# animal_1.type = "York"
# animal_repository.update(animal_1)

# vet_2 = Vet("Bob", "0900-3444567", "working")
# vet_repository.save(vet_2)
# print(vet_repository.select(vet_2.id).__dict__)


# all_animals = animal_repository.select_all()
# for animal in all_animals:
#     print(animal.__dict__)

all_vets = vet_repository.select_all()
for vet in all_vets:
    print(vet.__dict__)