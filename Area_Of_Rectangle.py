# Write a program to create a function to calculate the area of rectangle and the function must return the value.
def Area_of_Rectangle(l, b):
    return l * b

l = int(input("Enter the length of rectangle:"))
b = int(input("Enter the breadth of rectangle:"))

result = Area_of_Rectangle(l, b)
print("The Area of Rectangle:", result)
