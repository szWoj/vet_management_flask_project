import unittest

from django.test import TestCase

from models.vet import *

class VetTest(unittest.TestCase):

    def setUp(self):
        self.vet = Vet("Mark Robson", "07911-123456", "sick")

    def test_vet_has_name(self):
        self.assertEqual("Mark Robson", self.vet.name)
    def test_vet_has_contact(self):
        self.assertEqual("07911-123456", self.vet.contact)
    def test_vet_has_status(self):
        self.assertAlmostEqual("sick", self.vet.status)
