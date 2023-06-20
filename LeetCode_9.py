# Given an integer x, return true if x is a
# palindrome and false otherwise.

number = int(input('Number: '))
# print (str(number))
# print(str(number)[::-1])
#
# if str(number) == str(number)[::-1]:
#     print('Number is  a palindrome')
# else:
#     print('Number is not a palindrome')

print('Number is  a palindrome') if str(number) == str(number)[::-1] else print('Number is not a palindrome')