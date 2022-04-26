from random import *
import string
from user import user
from credentials import credentials

def create_user(firstname,lastname,username,userpassword):
  newuser= user(firstname,lastname,username,userpassword)
  return newuser

def login(userpassword ,username):
    print("Enter Your userame")
    loginUsername=input()
    print("Enter password")
    loginpassword=input()
    return userpassword==loginpassword and username==loginUsername



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
    
# def find_account(number):
#     return credentials.find_by_number(number)

def display_accounts():
    return credentials.display_accounts()


def main():
    # while True:
        print("Welcome to passwordLocker select SU to proceed")
        print("SU ")
        option=input()

        if option =="SU":
           print("Create Account")
           print("-")
           print("Enter your First Name")
           firstname=input()

           print("Enter your Last Name")
           lastname=input()

           print("Enter your User Name")
           username=input()

           print("set your  Password")
           userpassword=input()


           create_user(firstname,lastname,username,userpassword)
           print("your account was succesfully created below are your credentials")
           print("-"*7)

           print(f'Name:{firstname}{lastname}\nUsername{username}\nPassword{userpassword}')
           print("\nUse loginto your account using your credentials")
           print("\n \n ")
           

           successfull=login(username,userpassword)
           while successfull:
        # elif option =="LI":
        #    print("Enter Your userame")
        #    loginUsername=input()
        #    print("Enter password")
        #    loginpassword=input()
            #  login(username,userpassword)

        #    if successfull:
               print("\n")
               print("Go ahead create as many accounts as you wish and(MA) view them (VA")
               print("_"*50)
               print("MA -or-VA")
        
               choose=input()
               print("\n")

               if choose == "MA":

                 print("add your credentials and accounts")
                 print("-"*25)

                 accountusername=input("loginUsername")
                 print("Account name")
                 accountname=input()
                 print("\n")
                 print("Generate (GP)or create new password(NP)")
                 decision=input()
         

                 if decision =="GP":
                   characters=string.ascii_letters + string.digits
                   accountpassword="-".join(choice(characters)for x in range(randint(6,16)))
                   print(f"password{accountpassword}")
                   save_account(create_account(accountusername,accountname,accountpassword))
                   print(f'username:{accountusername}\n Account Name{accountname}\nPassword{accountpassword}')
                    
        
                 elif decision == "NP":
                   print("enter your password")
                   accountpassword=input()
                   save_account(create_account(accountusername,accountname,accountpassword))
                   print(f'username:{accountusername}\n Account Name{accountname}\nPassword{accountpassword}')


                 else:
                   print("Kindly key in a valid choice")
                  #  save_account(create_account(accountusername,accountname,accountpassword))
                  #  print("\n") 
                   print(f'username:{accountusername}\n Account Name{accountname}\nPassword{accountpassword}')

               elif choose == "VA":
                   if display_accounts():
                     print("view list of your created accounts")
                     print("-"*25)
                     for user in credentials.display_accounts():

                      print(f"Accounts:{user.accountname}\nPassword{user.accountpassword}\n\n")
                   else:
                     print("invalid credentials")

               else:
                print(" try again!")
                print("\n")
                break
            

        #  else:
        #      print("BYE")
        #      print("\n")
        #      break
             
if __name__ == '__main__':

    main()