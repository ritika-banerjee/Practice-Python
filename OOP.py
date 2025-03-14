# object oriented programming

class Animal:
    
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(self.name + " speaks")
        
    def show(self):
        print("I am " + self.name)
        
class Dog(Animal):
    
    def __init__(self, name):
        super().__init__(name) # references the parent class
    
    def bark(self):
        print(self.name + " bark")
        
    def set_name(self, name):
        self.name = name
        print("Name changed to " + self.name)
        
class Cat(Animal):

    def meow(self):
        print(self.name + " meow")
        
    def set_name(self, name):
        self.name = name
        print("Name changed to " + self.name)
    
d = Dog("Dog")
d.show()
d.speak()

c = Cat("Cat")
c.show()
c.speak()