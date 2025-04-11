# Create Class
print("Create Class")
class my:
    x=5

print(my)
print(my.x)


# Create Object
print("Create Object")

class my1:
    y=50

p1 = my1();  # Object p1

print(p1)
print(p1.y)

#__init__function
print("__init__function")

class my2:
    def __init__(self,name,age):
        self.name= name
        self.age = age
    
person = my2("Naman",18)

print(person.name)
print(person.age)

#__str__function
print("__str__function")

class my3:
    def __init__(self,name,age,place):
        self.name = name
        self.age = age
        self.place = place
    
    def __str__(abc):
        return f"{abc.name} ({abc.age}) - {abc.place}"
    
personObject = my3("Virat",18,"Delhi")

print(personObject)


#Object Methods

class myClass:
    def __init__(self,name,age,stats):
        self.name = name
        self.age = age
        self.stats= stats

    def myfunc(abc):
        print("Hello ",abc.name)

person = myClass("Vanshi",19,26)
print(person.name)
print(person.age)

person.myfunc()

person.age = 20   #Object modification
print(person.age)

del person.age    #Object property deletion
# print(person.age) #Error 

del person            #Object Deletion
print(person.name)



