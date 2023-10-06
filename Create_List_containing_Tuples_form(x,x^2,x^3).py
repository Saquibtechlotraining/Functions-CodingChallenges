# Write a python function to create and return a list containing tuples of the form (x, x^2, x^3)
# for all x between 1 and 20(both included).
def power_list():
    list = []
    for x in range(1, 21):
        list.append((x, x**2, x**3))
    return list

print(power_list())

