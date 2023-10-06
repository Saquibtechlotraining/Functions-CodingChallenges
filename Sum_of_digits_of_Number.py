# Write a Python function to find the sum of the digits of a given number.
# WRONG CODE---
def Sum_of_digits(number):
    str_number = str(number)                                     # '452'
    list_str_numbers = list(str_number)                          # ['4', '5', '2']
    for value in range(0, len(list_str_numbers)):
        list_str_numbers[value] = int(list_str_numbers[value])   #  [4, 5, 2]
    return sum(list_str_numbers)                                 #  11

number = int(input("Enter the number:"))  # 452
print(f"Sum of the digits of {number}:", Sum_of_digits(number))  # Output: 11
