import unittest
from models.feedback import Feedback
from models.owner import Owner

class FeedbackTest(unittest.TestCase):
    def setUp(self):
        owner = Owner('Jack', 'White', 'jwhite@outlook.com', '487239847', True, id = 5)
        self.feedback = Feedback(1, 2, 3, 4, 'sugg', 'oth', owner, 6 )
    
    def test_qos(self):
        self.assertEqual(1, self.feedback.qos)

    def test_fs(self):
        self.assertEqual(2, self.feedback.fs)

    def test_cf(self):
        self.assertEqual(3, self.feedback.cf)

    def test_recommend(self):
        self.assertEqual(4, self.feedback.recommend)

    def test_suggestions(self):
        self.assertEqual('sugg', self.feedback.suggestions)

    def test_other_comment(self):
        self.assertEqual('oth', self.feedback.other_comment)
    
    def test_owner_id(self):
        self.assertEqual(5, self.feedback.owner.id)

    def test_id(self):
        self.assertEqual(6, self.feedback.id)
