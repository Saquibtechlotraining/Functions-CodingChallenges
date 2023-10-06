# A palindrome is a word or phrase which reads the same in both directions.
# Given below are some palindromic strings:
# deed
# level
# Malayalam
# Rats live on no evil star
# Murder for a jar of red rum
#
# Write a program that defines a function ispalindrome() which checks whether a given string is a palindrome or not.
# Ignore spaces and case mismatch while checking for palindrome.
def ispalindrome(sentence):
    reverse_sentence = palindrome_sentence[::-1]

    if palindrome_sentence == reverse_sentence:
        return "String is Palindrome"
    else:
        return "String is not Palindrome"


palindrome_sentence = input("Enter the palindromic sentence:").replace(" ","").lower()
print(ispalindrome(palindrome_sentence))

