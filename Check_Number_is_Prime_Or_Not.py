# Write a python program to check whether the number is prime or not using functions.
def Check_prime(number):
    if (number % 2) != 0:
        return "prime number"
    else:
        return "not prime number"

number = int(input("Enter the number:"))
if number >= 2:
    print(f"{number} is", Check_prime(number))
else:
    print(f"Cannot take {number} to check")
