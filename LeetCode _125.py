# A phrase is a palindrome if, after converting all uppercase letters into
# lowercase letters and removing all non-alphanumeric characters, it reads the same
# forward and backward. Alphanumeric characters include letters and numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.

def isPalindrome(s):
    aux_array = [i.lower() for i in list(s) if i.lower() in list('abcdefghijklmnopqrstuvwxyz0123456789')]
    print(aux_array)
    return ''.join(aux_array) == ''.join(aux_array)[::-1]

print(isPalindrome('race a car'))

