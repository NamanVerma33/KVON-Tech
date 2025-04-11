# Create an Animal Class:
# Animal Class: Attributes: Name, Sound
# Dog Class: Inherits Animal, Add Bark sound
# Cat Class: Inherits Animal, Add Meow sound

class Animal:
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound

    def displayAnimal(self):
        print(f"Animal name is {self.name} and its produces{self.sound}")

class Dog(Animal):
    def __init__(self,name,sound):
        super().__init__(name, sound)
        

class Cat(Animal):
    def bark(self):
        self.displayAnimal()



d1 = Dog("Dog","Bark")
d1.displayAnimal()

c1 = Cat("Cat","Meow")
c1.bark()

