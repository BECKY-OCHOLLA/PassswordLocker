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


