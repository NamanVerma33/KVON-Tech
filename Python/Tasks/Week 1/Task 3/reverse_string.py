# Implement a function that reverses a given string without using built-in functions.

# User Input
userString = input("Enter the string ")

#Function that reverse the user string using list.
def reverseString(str):
    str_list = list(str);
    i = 0
    j = len(str_list) - 1
    while (i<j):
        str_list[i], str_list[j] = str_list[j], str_list[i]
        i += 1
        j -= 1
        s = "".join(str_list)
    print(s)

#Function that reverse the user string using slicing.
def reverseWithSlicing(str1):
    result = str1[::-1]
    return result

#Function Calling
reverseString(userString)

print("With the help of slicing, we Reverse:",reverseWithSlicing(userString))