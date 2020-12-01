import unittest

from models.testimonial import Testimonial
from models.owner import Owner

class TestimonialTest(unittest.TestCase):
    def setUp(self):
        owner = Owner('Jack', 'White', 'jwhite@outlook.com', '487239847', True, id = 3)
        self.testimonial = Testimonial('this is a testimonial', owner, 2)
    
     
    def test_testimonial(self):
        self.assertEqual('this is a testimonial', self.testimonial.testimonial)

    def test_owner_id(self):
        self.assertEqual(3, self.testimonial.owner.id)

    def test_id(self):
        self.assertEqual(2, self.testimonial.id)
