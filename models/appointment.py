class Appointment:
    def __init__(self, date, time, vet, animal, checked_in = False, id = None):
        self.date = date
        self.time = time
        self.vet = vet
        self.animal = animal
        self.checked_in = checked_in
        self.id = id

    def mark_checked_in(self):
        self.checked_in = True
        