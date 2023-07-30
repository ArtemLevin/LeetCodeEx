# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word
# or phrase, typically using all the original letters exactly once.
from collections import Counter
import copy
def isAnagram(s, t):
    c_s = copy.copy(s)
    copy_s = list(c_s)
    list_t = list(t)
    if len(list_t) == len(copy_s):
        for symbol in list(s):
            copy_s.remove(symbol)
            if symbol in list_t:
                list_t.remove(symbol)
        if len(list_t) == 0 and len(copy_s) == 0:
            return True
        else: return False
    else: return False

print(isAnagram("ab", 'a'))