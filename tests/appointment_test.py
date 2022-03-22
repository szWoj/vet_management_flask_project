import unittest

from models.appointment import *

class AppointmentTest(unittest.TestCase):

    def setUp(self):
        self.appointment = Appointment("03-05-2021", "17:30", 1, 2)
    
    def test_appointment_has_date(self):
        self.assertEqual("03-05-2021", self.appointment.date)
    def test_appointment_has_time(self):
        self.assertEqual("17:30", self.appointment.time)
    def test_appointment_has_time(self):
        self.assertEqual("17:30", self.appointment.time)
    def test_appointment_has_vet(self):
        self.assertEqual(1, self.appointment.vet)
    def test_appointment_has_animal(self):
        self.assertEqual(2, self.appointment.animal)
    def test_appointment_has_checked_in_false(self):
        self.assertEqual(False, self.appointment.checked_in)
    def test_appointment_has_mark_checked_in_method(self):
        self.appointment.mark_checked_in()
        self.assertEqual(True, self.appointment.checked_in)