from typing_extensions import Self
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
    self.new_User = user("Becky","2022") # create contact object

def test_init_(self):
    '''
    test if the objects have been initialized properly
    '''
    self.assertEqual(self.new_user.user_name,"Becky")
    self.assertEqual(self.new_user.password,"2022")

def test_save_user(self):
    '''
    test-save user to check if the user has been saved
    '''
    self.new_User.save_user() #saving the new user
    self.assertEqual(len(user.user_list),1)

def test_save_multiple_contact(self):
    '''
    test_save_multiple_contact to check if we can save multiple contact
    objects to our contact_list
    '''
    self.new_user.save_contact()
    test_user = user("Test","user","0712345678","test@user.com") # new contact
    test_user.save_user()
    self.assertEqual(len(user.user_list),2)
    