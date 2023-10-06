# Write a Python program to count the number of vowels in a string.
def Count_Vowels(string):
    s_string = string.replace(" ","")
    vowels = "AEIOUaeiou"
    count = 0
    for char in s_string:
        if char in vowels:
            count = count + 1
    return count

string = input("Enter the string to count vowels:")
print(F"Number of vowels in {string} is:", Count_Vowels(string))
