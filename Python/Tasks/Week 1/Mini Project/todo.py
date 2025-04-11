# Build a to-do list application using a dictionary where users can add tasks, mark them as completed, and view pending/completed tasks.


toDo = {"Buy Milk": "Pending",
        "Sell bike" : "Completed"}

def operations():
    print("\n1)Add task in the ToDO List.")
    print("2)Mark status completed in the ToDO List.")
    print("3)View Pending tasks in the ToDO List.")
    print("4)View Completed task in the ToDO List.")
    print("5)Show ToDO List")
    print("6)Exit")

def addTask():
    taskName = input("Enter the task name").strip()
    toDo.update({taskName:"Pending"})

def status():
    taskName = input("Enter the task name of which you want to check status")
    if taskName in toDo:
        print(f"{taskName} Status is {toDo[taskName]}")
        if toDo[taskName]=="Pending":
            toDo[taskName]="Completed"
            print("Mark To-")
            print(f"{taskName} Status is now {toDo[taskName]}")
    else:
        print("Task name you enter is not in the ToDo list. Please Try again")

def pending():
    print("List of Pending tasks in the To Do")
    if toDo:
        flag=1
        for taskName,taskStatus in toDo.items():
            if taskStatus=="Pending":
                flag=0
                print(f"Task Name-{taskName}\tTask Status-{taskStatus}")
        if flag:
            print("All tasks are completed in the list")
    else:
        print("No tasks in the record")
def completed():
    print("List of Completed tasks in the To Do")
    if toDo:
        flag=1
        for taskName,taskStatus in toDo.items():
            if taskStatus=="Completed":
                flag=0
                print(f"Task Name-{taskName}\tTask Status-{taskStatus}")
        if flag:
            print("All tasks are pending in the list")
    else:
        print("No tasks in the record")

def display():
    if toDo:
        for taskName, taskDetails in toDo.items():
            print(f"Task Name-{taskName}\tTask Status-{taskDetails}")
    else:
        print("No tasks in the record")

def main():
    operations()
    while(True):
        try:
            choice = int(input("Enter the operation you want to perform: "))
            if choice==1:
                addTask()
            elif choice==2:
                status()
            elif choice==3:
                pending()
            elif choice==4:
                completed()
            elif choice==5:
                display()
            else:
                print("Exit")
                break
        except ValueError:
            print("Please enter the integer value.Try again")

main()


