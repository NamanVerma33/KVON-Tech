# Exception Handling Task:
# Create a Python program that:
# Asks the user for 2 numbers.
# Performs division.
# Handle ZeroDivisionError and ValueError.



def division(num1,num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        return ("Zero Division is not allowed. Error -",ZeroDivisionError)
         
flag= True
while(flag):
    try:
        num1 = float(input("Enter the first number"))
        num2 = float(input("Enter the second number"))
        flag=False
    except ValueError:
        print("Please Enter the number only.Error -",ValueError)


print(division(num1,num2))
