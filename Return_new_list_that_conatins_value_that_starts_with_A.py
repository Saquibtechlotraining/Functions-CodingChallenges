# Write a Python function that takes a list of strings as input and returns a new list
# containing only the strings that start with the letter 'A'.
def filter_strings(size):
    list = []
    new_list = []
    for i in range(0, size):
        value = input(f"Enter the {i+1} value:")
        list.append(value)

    for val in list:
        if val.startswith("A") or val.startswith("a"):
            new_list.append(val)

    return list, new_list

size = int(input("Enter the size of the list:"))
org_list, newly_list = filter_strings(size)
print("Original List:", org_list)
print("List that contains only values that startswith A:", newly_list)