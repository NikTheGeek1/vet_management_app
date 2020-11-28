import unittest
from models.owner import Owner

class OwnerTest(unittest.TestCase):
    def setUp(self):
        self.owner = Owner('James', 'Black', 'jblack@outlook.com', '+44 7422 449 29 44', True, 4)

    def test_fist_name(self):
        self.assertEqual('James', self.owner.first_name)

    def test_last_name(self):
        self.assertEqual('Black', self.owner.last_name)

    def test_email(self):
        self.assertEqual('jblack@outlook.com', self.owner.email)
     
    def test_phone(self):
        self.assertEqual('+44 7422 449 29 44', self.owner.phone)
    
    def test_registered(self):
        self.assertEqual(True, self.owner.registered)
    
    def test_id(self):
        self.assertEqual(4, self.owner.id)