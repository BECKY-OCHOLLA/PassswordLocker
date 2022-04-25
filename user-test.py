import unittest #importing the unittest module
from user import user #importing the user class

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

def setUp(self):
    '''
    set up method to run before each test case
    '''
    self.new_User = user("Becky","Ocholla","2022") # create contact object