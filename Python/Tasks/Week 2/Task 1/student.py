# Create a Student Class:
# Attributes: Name, Roll Number, Marks
# Methods:
# get_details() → Print name, roll number, marks
# is_passed() → Check if marks > 33 then passed else failed


class Student:
    def __init__(self,name,rNo,marks):
        self.name = name
        self.rNo = rNo
        self.marks = marks

    def get_details(self):
        print("Name",self.name)
        print("Roll No",self.rNo)
        print("Marks",self.marks)

    def is_passed(self):
        if self.marks>33:
            print("Passed")
        else:
            print("Failed")
    
record = int(input("How many students record you want to enter"))

# i = 0
while (record!=0):
    name = input("Enter the name of student")
    rollNo = int(input("Enter the roll no of student"))
    marks = int(input("Enter the marks of student"))
    student1 = Student(name,rollNo,marks)
    student1.get_details()
    student1.is_passed()
    record-=1


