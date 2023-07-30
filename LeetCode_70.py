# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
import copy

def climbStairs(n):
    if len(n) == 1 or len(n) == 0:
        return "nothing to remove"
    else:
        m = copy.copy(n)
        n.pop(0)
        del m[0:2]
        climbStairs(n)
        climbStairs(m)



print(climbStairs([1,1,1,1]))