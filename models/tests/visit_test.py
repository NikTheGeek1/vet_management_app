import unittest
import datetime as dt
from models.visit import Visit

class VisitTest(unittest.TestCase):
    def setUp(self):
        self.visit = Visit(
            1,
            dt.date(2020, 4, 20),
            dt.date(2020, 4, 20),
            'just a visit',
            4
        )
    
    def test_pet_id(self):
        self.assertEqual(1, self.visit.pet_id)

    def test_check_in(self):
        self.assertEqual(dt.date(2020, 4, 20), self.visit.check_in)

    def test_check_out(self):
        self.assertEqual(dt.date(2020, 4, 20), self.visit.check_out)    
