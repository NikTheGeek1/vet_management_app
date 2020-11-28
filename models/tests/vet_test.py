import unittest

from models.vet import Vet

class VetTest(unittest.TestCase):
    def setUp(self):
        self.vet = Vet('Helen', 'Kiri', 4)

    def test_first_name(self):
        self.assertEqual('Helen', self.vet.first_name)

    def test_last_name(self):
        self.assertEqual('Kiri', self.vet.last_name)

    def test_id(self):
        self.assertEqual(4, self.vet.id)

