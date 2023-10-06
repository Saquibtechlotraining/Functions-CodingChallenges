# Find the area of rectangle:-
def area_rectangle(length, breadth):
    if type(length) is  not str  and type(breadth) is not  str:
        return length * breadth
    else:
        return "Wrong value type"

print("Area of rectangle:", area_rectangle(3,5))
