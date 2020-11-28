import unittest

from models.pet_treatment import PetTreatment

class PetTreatmentTest(unittest.TestCase):
    def setUp(self):
        self.pet_treatment = PetTreatment(2, 1, 3)

    def test_treatment_id(self):
        self.assertEqual(1, self.pet_treatment.treatment_id)

    def test_pet_id(self):
        self.assertEqual(2, self.pet_treatment.pet_id)
    
    def test_id(self):
        self.assertEqual(3, self.pet_treatment.id)
    