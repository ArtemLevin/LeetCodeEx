# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
import copy


def climbStairs(n):
    memo = {}
    memo[1] = 1
    memo[2] = 2

    def climb(n):
        if n in memo:
            return memo[n]
        else:
            memo[n] = climb(n - 1) + climb(n - 2)
            return memo[n]

    return climb(n)


print(climbStairs(4))
