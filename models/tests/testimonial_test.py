import unittest

from models.testimonial import Testimonial

class TestimonialTest(unittest.TestCase):
    def setUp(self):
        self.testimonial = Testimonial('this is a testimonial', 3, 2)
    
     
    def test_testimonial(self):
        self.assertEqual('this is a testimonial', self.testimonial.testimonial)

    def test_owner_id(self):
        self.assertEqual(3, self.testimonial.owner_id)

    def test_id(self):
        self.assertEqual(2, self.testimonial.id)
