class Profile:
    def __init__(self, email, password):
       self.__email = email
       self.__password = password

    def setemail(self, email):
        self.__email = email
        
    def chkpass(self, pwd):
        return pwd == self.__password
        
    def displayemail(self):
        return self.__email
       

p = Profile("sukhmani@example.com", "secure123")
print(p.displayemail())
print(p.chkpass("wrongpass"))
print(p.chkpass("secure123"))
p.setemail("newemail@example.com")
print(p.displayemail())
