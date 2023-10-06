# Write a Python function that takes a list of numbers as input and returns the average
# of all the numbers in the list.
def average_of_all_numbers(size):
    if size != 0:
        list = []
        for i in range(0, size):
            value = int(input(f"Enter the {i+1} value:"))
            list.append(value)

        average_of_all = sum(list) / len(list)
        return average_of_all
    else:
        return None

size = int(input("Enter the size of the list:"))
print(average_of_all_numbers(size))

