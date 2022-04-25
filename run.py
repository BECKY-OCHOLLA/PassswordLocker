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
  newaccount= credentials(accountusername,accountname,accountpassword)
  return newaccount

def save_account(user):
   return user.save_account()

def delete_account(user):
   return user.delete_account()
    
def find_account(number):
    return credentials.find_by_number(number)


def main():
    while True:
        print("Karibu passwordLocker andika SU au LI ili uweze kuendelea")
        print("SU -au- LI")

    if option =="SU":
        print("Create Account")
        print("-"*7)
        print("Enter your First Name")
        firstname=(input)

        print("Enter your Last Name")
        lastname=(input)

        print("Enter your User Name")
        username=(input)

        print("set your  Password")
        userpassword=(input)


        save_user(create_user(firstname,lastname,username,userpassword))
        print("your account was succesfully created below are your credentials")
        print("-"*7)

        print(f'Name:{firstname}{lastname}\nUsername{username}\nPassword{userpassword}')
        print("\nUse login to your account using your credentials")
        print("\n \n ")

    elif option =="LI":
        
        
        

