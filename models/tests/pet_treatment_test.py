import unittest
import datetime as dt
from models.pet_treatment import PetTreatment
from models.pet import Pet
from models.vet import Vet
from models.owner import Owner
from models.treatment import Treatment

class PetTreatmentTest(unittest.TestCase):
    def setUp(self):
        owner = Owner('Jack', 'White', 'jwhite@outlook.com', '487239847', True, id = 3)
        vet = Vet('White', 'Jack', 3)
        pet = Pet('dummy pet', dt.date(2020,2,2), '1', 'dog', owner, vet, 'dkfj', 'what', 2)
        treatment = Treatment('kadjf', 'a description', 1)
        self.pet_treatment = PetTreatment(pet, treatment, 3)

    def test_treatment_id(self):
        self.assertEqual(1, self.pet_treatment.treatment.id)

    def test_pet_id(self):
        self.assertEqual(2, self.pet_treatment.pet.id)
    
    def test_id(self):
        self.assertEqual(3, self.pet_treatment.id)
    