# File Handling Task:
# Create a text file called students.txt
# Allow user to enter Name, Age, Marks and save in file.
# Read and display file contents.


print("Student Record management\nEnter any number of records you want to save.\nIf you want to exit type Yes otherwise No")
i = 1
f = open("student.txt","+at")
while(True):
    students = {
        "Name" : input("Enter the name"),
        "Age" : int(input("Enter the age")),
        "Marks" : float(input("Enter the marks"))
    }
    f.write((f"\nStudent {i}\nName : {students["Name"]}\nAge : {students["Age"]}\nMarks : {students["Marks"]} "))
    i+=1

    choice = input("Enter Yes if you dont want to add more data otherwise No")
    if choice=="Yes":
        break

f.seek(0)
print("The Student Record saved in file are : ")
print(f.read())
f.close()

