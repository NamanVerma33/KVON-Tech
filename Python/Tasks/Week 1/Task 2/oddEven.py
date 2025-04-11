# Write a program that asks the user for a number and checks if it's even or odd.

userInput = int(input("Enter the number: "))

if (userInput%2)==0:
    print(userInput ,"is even")
else:
    print(userInput, "is odd")