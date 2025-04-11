students={"Naman":90,"Harshit":"88"}
def options():
    print("1)Show the students record")
    print("2)Search the student name in the dictionary")
    print("3)Add a student in the dictionary")
    print("4)Update the student marks in the dictionary")
    print("5)Exit")

def showStudents():
    if students:
        for name,marks in students.items():
            print(f"Name : {name} , Marks: {marks}")
    else:
        print("\nNo record found")

def searchStudent():
    sName = input("Enter the name of the student you want to search: ").strip()
    if students:
        flag=1
        for name,marks in students.items():
            if(name==sName):
                flag=0
                print(f"Student name {name} you search marks is {marks}")
    
        if(flag):
            print(f"Student name {sName} not exist in students record")
    else:
        print("\nNo record found")
    
def addStudent():
    sName = input("Enter the name you want to add")
    marks = int(input("Enter the marks of the student"))
    students.update({sName:marks})
    showStudents()

def updateStudent():
    sName = input("Enter the name of the student you want to update marks").strip()
    if sName in students:
        updateMarks = int(input(f"Enter the updated marks of {sName}"))
        students[sName]=updateMarks
    else:
        print("Student not exist")


def display():
    options()
    while True:
        choice = int(input("Choose the operation you want to perform from 1-5 "))
        if choice==1:
            showStudents()
        elif choice==2:
            searchStudent()
        elif choice==3:
            addStudent()
        elif choice==4:
            updateStudent()
        elif choice==5:
            print("Exit")
            break
        else:
            print("Please enter between 1-5")
            
display()