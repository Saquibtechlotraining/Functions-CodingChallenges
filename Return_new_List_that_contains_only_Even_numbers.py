# Write a Python function that takes a list of numbers as input and returns a new list containing only the
# even numbers from the input list:-
def contain_only_even(size):
    list = []
    new_list = []
    for i in range(0, size):
        value = int(input(f"Enter the {i+1} value:"))
        list.append(value)

    for val in list:
        if val % 2 == 0:
            new_list.append(val)
    return list, new_list        # Multiple returns


size = int(input("Enter the size of the list:"))

org_lis, new_lis = contain_only_even(size)
print("Original list:", org_lis)
print("new_list contains only even numbers:", new_lis)