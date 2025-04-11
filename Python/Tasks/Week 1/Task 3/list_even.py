# Write a function that takes a list of numbers and returns a new list with only even numbers.

count = int(input("Enter the number of items you want to add "))
listNumbers = []
while count!=0:
    listNumbers.append(int(input()))
    count-=1

print("Original List" ,listNumbers)

new = []

def list_even(list):
    for number in list:
        if(number%2==0):
            new.append(number)
            
    if(len(new)==0):
        return "No even number found in the list"
    else:
        return new

print("New List" ,list_even(listNumbers))