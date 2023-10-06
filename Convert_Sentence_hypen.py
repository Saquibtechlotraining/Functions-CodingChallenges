# Write a python program that accepts a hypen-separated sequence of words as input and calls a
# function convert() which converts it into a hypen-separated sequence after sorting them alphabetically.
# For example, if the input string is

# 'here-come-the-dots-followed-by-dashes'
# then the converted string should be
# by-come-dashes-dots-followed-here-the

def convert(sentence):

    list_sentence = sentence.split("-")      # ['here', 'come', 'the', 'dots', 'followed', 'by', 'dashes']
    sentence_sorted = sorted(list_sentence)  # ['by', 'come', 'dashes', 'dots', 'followed', 'here', 'the']
    return ("-".join(sentence_sorted))

sentence = "here-come-the-dots-followed-by-dashes"
print(convert(sentence))