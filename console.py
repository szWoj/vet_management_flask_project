from models.animal import Animal
from models.appointment import Appointment
from models.vet import Vet

from repositories import appointment_repository, vet_repository, animal_repository

# animal_1 = Animal("Meg", "03-02-2021", "pudel", "07911-123456", "regular check-up")
# animal_repository.save(animal_1)

# print(animal_repository.select(animal_1.id).__dict__)

# animal_repository.delete(2)
# animal_1.type = "York"
# animal_repository.update(animal_1)

# vet_4 = Vet("Frank", "0900-3444567", "on leave")
# vet_repository.save(vet_4)
# print(vet_repository.select(vet_2.id).__dict__)
# vet_4.status = "sick"
# vet_repository.update(vet_4)

# all_animals = animal_repository.select_all()
# for animal in all_animals:
#     print(animal.__dict__)
# vet_repository.delete(2)
# vet_1 =Vet("Rob", "0900-34567", "sick")
# vet_repository.save(vet_1)
# vet_2 =Vet("Markk", "0900-3444567", "working")
# vet_repository.save(vet_2)

# animal_1 = Animal("Meg", "03-02-2021", "pudel", "07911-123456", "regular check-up", vet_1)
# animal_repository.save(animal_1)
# animal_2 = Animal("Mog", "04-06-2021", "cat", "0791-3456", "regular check-up", vet_2)
# animal_repository.save(animal_2)

# appointment1 = Appointment("03-02-2021", "17:30", vet_1, animal_1)
# appointment_repository.save(appointment1)

# appointment2 = Appointment("01-02-2021", "14:30", vet_2, animal_2)
# appointment_repository.save(appointment2)

# all_animals = animal_repository.select_all()
# for animal in all_animals:
#     print(animal.__dict__)

all_appointments = appointment_repository.select_all()
for appointment in all_appointments:
    print(appointment.__dict__)

# all_vets = vet_repository.select_all()
# for vet in all_vets:
#     print(vet.__dict__)


