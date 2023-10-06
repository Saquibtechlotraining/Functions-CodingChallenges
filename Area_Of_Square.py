# Write a python program to create a function area_of_square(side) and
# calculate the area of square through taking input from user.
def area_of_square(side):
    result = side * side
    return result

side = int(input("Enter the length of the side:"))
output = area_of_square(side)
print(f"Area of Square of side {side}:", output)

