f = open("Employee Details.txt","a")
class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def Display(self):
        f.write((f"\nName-{self.name}\nAge-{self.age}\nSalary-{self.salary}"))

choice = True
i=1
while(choice):
    name = input("Enter the name")
    age = int(input("Enter the age"))
    salary = int(input("Enter the salary"))
    emp = Employee(name,age,salary)
    f.write(f"\nEmpoyee{i}")
    emp.Display()
    i+=1
    choice = input("Want to enter more empoyees data in the file:Type Yes or No")
    if choice == "No":
        f.close()
        break


f = open("Employee Details.txt")
print(f.read())
