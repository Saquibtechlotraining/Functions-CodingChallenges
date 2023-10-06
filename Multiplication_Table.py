# Write a Python program to print the multiplication table of a given number(using functions).
def table(num):
    for i in range(1, 11):
        print(f"{num} X {i} = {i*num}")

num = int(input("Enter the number of the table:"))
table(num)
