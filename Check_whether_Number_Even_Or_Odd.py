# Write a python program to check if the given number is even or odd using functions:-

# Using without return type:-
def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is Even Number")
    else:
        print(f"{number} is Odd Number")

number = int(input("Enter the number to be check:"))
check_even_odd(number)


# Using return type:-
def check_even_odd(number):
    if number % 2 == 0:
        return (f"{number} is Even Number")
    else:
        return (f"{number} is Odd Number")

number = int(input("Enter the number to be check:"))
print(check_even_odd(number))

