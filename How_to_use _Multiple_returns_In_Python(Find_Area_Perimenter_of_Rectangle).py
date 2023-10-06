# How to use to print Multiple returns in Python:-
def area_rectangle(len, b):
    area = len * b
    perimeter = 2 * (len + b)
    return area, perimeter      # Multiply returns in python

len = int(input("Enter the length of a rectangle:"))   # 2
b = int(input("Enter the breadth of a rectangle:"))    # 3

# Unpacking of tuples
ar, pe = area_rectangle(len, b)
print(f"Area of rectangle: {ar} and Perimeter of rectangle: {pe}")

