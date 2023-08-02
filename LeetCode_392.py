# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by deleting some
# (can be none) of the characters without disturbing the relative positions of the remaining
# characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

def isSubsequence(s, t):
    if len(s) == 0 and len(t) == 0: return True
    elif len(s) >= len(t): return False
    else:
        for i in s:
            if i in t:
                t = t[t.index(i)+1:]
                print(f'{t =}')
            else:
                return False
    return True

print(isSubsequence("bb", "ahbgdc"))