# Pangram is a sentence that uses every letter of the alphabet. Write a program that checks whether a given
# string is pangram or not, through a user-defined function ispangram()

import string
sentence = input("Enter the sentence:").replace(" ","").lower()
sentence = "".join(sorted(set(sentence)))
#print(sentence)

pangram = "".join(list(string.ascii_lowercase))   # pangram stored all alphabet letter in lowercase in one string
#print(pangram)

if sentence == pangram:
    print("sentence is pangram")
else:
    print("sentence is not pangram")
