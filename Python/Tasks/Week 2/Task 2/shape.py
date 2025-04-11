class shape:
    def __init__(self,name):
        self.name = name

    def area(self,area):
        print(f"Area of {self.name} is {area}")

class Rectangle(shape):
    def __init__(self, name):
        super().__init__(name)


    def area(self,length,breadth):
        return length*breadth

class Circle(shape):
    def __init__(self, name):
        super().__init__(name)

    def area(self,radius):
        return 3.14*radius*radius

r1 = Rectangle("Rectangle")
Area_Rectangle=r1.area(10,4)
print(f"Area of Rectangle is {Area_Rectangle}")


c1 = Circle("Circle")
Area_Circle=c1.area(10)
print(f"Area of Circle is {Area_Circle}")


