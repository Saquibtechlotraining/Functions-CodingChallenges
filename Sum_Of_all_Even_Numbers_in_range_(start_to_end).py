# Write a python program to find the sum of all the even numbers between the range of start and end using functions.

# Using While Loop:-
def sum_even(start, end):
    sum_even = 0
    while (start <= end):
        if (start % 2) == 0:
            sum_even = sum_even + start
        else:
            pass
        start = start + 1

    print(f"Sum of even numbers in the range:", sum_even)

start = int(input("Enter the starting range:"))
end = int(input("Enter the ending range:"))
sum_even(start, end)


# Using for Loop:

def sum_even(start, end):
    sum_even = 0
    for i in range(start, end+1):
        if (i % 2) == 0:
            sum_even = sum_even + i
        else:
            pass
    return sum_even

start = int(input("Enter the starting range:"))
end = int(input("Enter the ending range:"))
result = sum_even(start, end)
print(f"Sum of even numbers in the range {start} to {end}:", result)

