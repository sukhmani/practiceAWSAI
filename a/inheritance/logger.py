class Person:
    def __init__(self, name, age):
       self.name = name
       self.age = age
       self.hobbies = ["reading", "coding"]
       

    def greet(self):
        print("Hello my name is" +str(self.name)+ " and I am" +str(self.age) +" years old.")

    def is_adult(self):
        return self.age >= 18
    
    def setage(self, nage):
        self.age = nage

    def showhobbies(self):
        print(str(self.hobbies))

    def addhobby(self, addh):
        self.hobbies.append(addh)

    def removehobby(self, removeh):
        self.hobbies.remove(removeh)
    

p = Person("Sukhmani", 25)
p.greet()
print(p.is_adult())
p.setage(21)


p.addhobby("a")
p.addhobby("b")
p.greet()
p.removehobby("a")
p.showhobbies()


