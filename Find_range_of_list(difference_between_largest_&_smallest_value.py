# Write a Python program that takes a list of numbers as input and outputs the range of the list
# (i.e. the difference between the largest and smallest values).

def find_range(size):
    list = []
    for i in range(0, size):
        value = int(input(f"Enter the {i+1} value:"))
        list.append(value)
    largest_value = max(list)
    smallest_value = min(list)
    return largest_value - smallest_value

size = int(input("Enter the size of the list:"))
print("find range:", find_range(size))

