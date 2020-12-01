import unittest
import datetime as dt
from models.pet import Pet
from models.vet import Vet
from models.owner import Owner
class PetTest(unittest.TestCase):
    def setUp(self):
        owner = Owner('Jack', 'White', 'jwhite@outlook.com', '487239847', True, id = 4)
        vet = Vet('White', 'Jack', 3)
        self.pet = Pet(
            'Smokey',
            dt.date(2020, 7, 24),
            '',
            'cat',
            owner,
            vet,
            'randomString',
            'dkfjd',
            3
        )

    def test_name(self):
        self.assertEqual('Smokey', self.pet.name)
    
    def test_dob(self):
        self.assertEqual(dt.date(2020, 7, 24), self.pet.dob)

    def test_yo(self):
        self.pet.dob_to_yo(self.pet.dob)
        self.assertEqual(0.04, self.pet.yo)

    def test_type(self):
        self.assertEqual('cat', self.pet.type)

    def test_owner(self):
        self.assertEqual(4, self.pet.owner.id)

    def test_vet(self):
        self.assertEqual(3, self.pet.vet.id)

    def test_image(self):
        self.assertEqual('randomString', self.pet.image64)