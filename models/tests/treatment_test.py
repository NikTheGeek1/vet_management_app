import unittest

from models.treatment import Treatment

class TreatmentTest(unittest.TestCase):
    def setUp(self):
        self.treatment = Treatment(
            'Anthelmintics',
            'These are used to eliminate parasitic worms, which infest their systems and steal important nutrients.'        
        )

    def test_title(self):
        self.assertEqual('Anthelmintics', self.treatment.title)

    def test_description(self):
        self.assertEqual('These are used to eliminate parasitic worms, which infest their systems and steal important nutrients.', self.treatment.description)