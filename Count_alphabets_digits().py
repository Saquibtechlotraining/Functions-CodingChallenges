# Write a program that defines a function count_alphabets_digits() that accepts a string and calculates the
# number of alphabets and digits in it. It should return these values as a dictionary.
def count_alphabets_digits(sentence):
    digits = 0
    alpha = 0
    for char in sentence:
        if char.isalpha():
            alpha += 1

        elif char.isnumeric():
            digits += 1

        else:
            pass

    return {"alphabets" : alpha, "digits" : digits}

sentence = "ahmad281%"
print(count_alphabets_digits(sentence))
