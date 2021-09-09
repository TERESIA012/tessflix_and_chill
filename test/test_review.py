import unittest
from app.models import Review
class ReviewTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_review = Review(1234,'Python Must Be Crazy','https://image.tmdb.org/t/p/w500/khsjha27hbs','A thrilling new Python Series')
    def test_save_review (self):
        '''
        testcase method to check if review can be saved
        '''