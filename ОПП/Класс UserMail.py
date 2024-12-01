class UserMail:
    def __init__(self, login, email):
        self.login = login
        self.__email = email 
        
    def get_email(self):
        return self.__email 
    
    
    def set_email(self, value):
        if isinstance (value, str) and value.count('@') == 1 and '.' in value[value.find('@'):]:
            self.__email = value
        else:
            raise ValueErroe(f"ErrorMail:{value}")

    email = property(fget=get_email,fset=set_email) 

try:
    UserMail('belosnezhka', {1, 2, 3})
except ValueError as e:
    print(e)