import string
# from random import
from user import user
from credentials import credentials

def create_user(firstname,lastname,username,userpassword):
  newuser= user(firstname,lastname,username,userpassword)
  return newuser

def save_user(user):
   return user.save_user()

def delete_user(user):
   return user.delete_user()
    
def find_user(number):
    return user.find_by_number(number)


def create_account(accountusername,accountname,accountpassword):
  newaccount= credentials(accountusername,accountname,accountpassword):
  return newaccount

def save_account(user):
   return user.save_account()

def delete_account(user):
   return user.delete_account()
    
def find_account(number):
    return credentials.find_by_number(number)