class credentials:
    '''
    class that generates new instances of credentials
    '''
    accounts=[]

def __init__(self,accountusername,accountname,accountpassword):
    '''
    _init_ methot that help use to define properties for object self
    '''
    self.accountusername = accountusername
    self.accountname = accountname
    self.accountpassword = accountpassword

def save_account(self):
    '''
    save_account method saves credentials into accounts
    '''  

    credentials.accounts.append(self)

def delete_account(self):
    '''
    delete account method used to delete credentials from accounts
    '''
    credentials.accounts.remove(self)

@classmethod
def display_accounts(cls):
    '''
    method that returns info from the accounts

    '''
    for accounts in cls.accounts:
      return cls.accounts


@classmethod
def find_by_number(cls,number):
    '''
    the method takes in a user name and returns a contact that matches that number
    '''
    for accounts in cls.accounts:
        if accounts.accountusername == number:
            return accounts


