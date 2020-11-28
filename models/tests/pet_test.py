import unittest
import datetime as dt
from models.pet import Pet

class PetTest(unittest.TestCase):
    def setUp(self):
        self.pet = Pet(
            'Smokey',
            dt.date(2020, 7, 24),
            '',
            'cat',
            4,
            3,
            'randomString'
        )

    def test_name(self):
        self.assertEqual('Smokey', self.pet.name)
    
    def test_dob(self):
        self.assertEqual(dt.date(2020, 7, 24), self.pet.dob)

    def test_yo(self):
        self.pet.dob_to_yo()
        self.assertEqual(0.04, self.pet.yo)

    def test_type(self):
        self.assertEqual('cat', self.pet.type)

    def test_owner(self):
        self.assertEqual(4, self.pet.owner_id)

    def test_vet(self):
        self.assertEqual(3, self.pet.vet_id)

    def test_image(self):
        self.assertEqual('randomString', self.pet.image)