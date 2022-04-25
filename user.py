from operator import truediv


class user:
    '''
    A class thatbgenerates new instance of users
    '''
    userslists=[]

def __init__(self,first_name,last_name,user_name,password):
    '''
    __init__ method that helps us define properties for our users.
    '''
        
    self.first_name = first_name
    self.last_name =last_name
    self.user_name = user_name
    self.password = password

def save_user(self):
    '''
    save_user method saves user intouserlists
    '''  
    user.userslists.append(self)  


@classmethod
def display_users(cls):
    '''
    method that returns info from the userlist
    '''
    for user in cls.userslists:
      return cls.userslists

@classmethod
def find_by_number(cls,number):
    '''
    the method takes in a user name and returns a user that matches that number
    '''
    for user in cls.userslists:
        if user.password == number:
            return user


@classmethod
def user_exist(cls,number):
    '''
    method that checks if a user exists
    '''

    for user in cls.userslists:
        if user.user_name == number:
            return True
            return False
      
