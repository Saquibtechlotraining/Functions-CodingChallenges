# Write a Python program to find the factorial of a number using functions.

def factorial(number):
    fact = 1
    for i in range(1, number+1):
        fact = fact * i
    return fact

number = int(input("Enter the number:"))
print(f"Factorial of {number} is :", factorial(number))

