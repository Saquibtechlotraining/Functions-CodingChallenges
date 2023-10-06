# Write a program that defines a function convert() that receives a string containing a sequence of whitespace
# separated words and returns a string after removing all duplicate words and sorting them alphnumerically.
# For example if the string passed to convert() is
# s = 'Sakhi was a singer because her mother was a singer, and Sakhi\'s mother was a singer because her father was a singer'.
#
# then, the output should be :
# Sakhi Sakhi's and because father her mother singer singer, was

# Method - 1
def convert(s):
    list_word = s.split()
    list_word.sort()
    result = []

    for value in list_word:
        if value not in result:
            result.append(value)
    return result

s = 'Sakhi was a singer because her mother was a singer, and Sakhi\'s mother was a singer because her father was a singer'
print("String after removing all duplicates words and sort them alphanumerically:", " ".join(convert(s)))

