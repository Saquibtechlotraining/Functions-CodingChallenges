# Write a python program to get the reverse of the string using functions.

# Using Return Type:-
def reverse_string(string):
    reversed_string = string[::-1]
    return reversed_string

string = input("Enter the string:")
print("Reversed String:", reverse_string(string))

