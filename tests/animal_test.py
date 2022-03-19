import unittest

from models.animal import *

class AnimalTest(unittest.TestCase):

    def setUp(self):
        self.animal = Animal("Rex", "03-05-2021", "pudel", "07911-123456", "Regular check-up")
        
    def test_animal_has_name(self):
        self.assertEqual("Rex", self.animal.name)
    def test_animal_has_dob(self):
        self.assertEqual("03-05-2021", self.animal.dob)
    def test_animal_has_type(self):
        self.assertAlmostEqual("pudel", self.animal.type)
    def test_animal_has_contact(self):
        self.assertEqual("07911-123456", self.animal.contact)
    def test_animal_has_notes(self):
        self.assertEqual("Regular check-up", self.animal.notes)
