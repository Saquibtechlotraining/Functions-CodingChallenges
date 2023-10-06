# Write a program to receive three integers from keyboard and get their sum and product
# calculated through a user-defined function cal_sum_prod().
def cal_sum_prod(num1, num2, num3):
    total_sum = num1 + num2 + num3
    total_product = num1 * num2 * num3

    return total_sum, total_product      # Multiple returns

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
num3 = int(input("Enter third number:"))

sum, product = cal_sum_prod(num1, num2, num3)    # calling of cal_sum_prod (function)
print(f"Total Sum of {num1} + {num2} + {num3}:", sum)
print(f"Total Product of {num1} * {num2} * {num3}:", product)
