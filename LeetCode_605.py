# You have a long flowerbed in which some of the plots are planted, and some are not.
# However, flowers cannot be planted in adjacent plots.
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty,
# and an integer n, return true if n new flowers can be planted in the flowerbed without
# violating the no-adjacent-flowers rule and false otherwise.
import math
from collections import Counter


def canPlaceFlowers(flowerbed, n):
    myStr = (''.join(str(i) for i in flowerbed)).split('1')
    counter = 0
    for i in myStr:
        counter += math.ceil(len(i)/3)
        print(f'{i = }, {counter = }, {math.ceil(len(i)/3) = }')
    print(f'{counter =}')
    return counter == n or counter > 0

flowerbed = [1,0,0,0,0,0,1]

print(canPlaceFlowers(flowerbed, 2))