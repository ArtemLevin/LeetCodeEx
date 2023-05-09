# Given n non-negative integers representing an elevation map where the width of each
# bar is 1, compute how much water it can trap after raining.

import random

n = int(input("Enter the number of lines ---> "))

waterArray = [random.randint(1, 10) for i in range(n)]
print(waterArray)
maxDot = max(waterArray)
i = 0
j = 0
while i < maxDot:
    tempMaxDot = maxDot - i
    j = 0
    while j < len(waterArray):
        if waterArray[j] < tempMaxDot:
            print("   ", end='')
        else:
            print(" * ", end='')
        j = j + 1
    print("")
    i = i + 1

maxValue = max(waterArray)

max_left = 0
max_right = 0
ans = 0
left = 0
right = len(waterArray) - 1
while left<right:
    if waterArray[left] < waterArray[right]:
        if waterArray[left] > max_left:
            max_left = waterArray[left]
        else:
            ans += max_left - waterArray[left]
        left += 1
    else:
        if waterArray[right] > max_right:
            max_right = waterArray[right]
        else:
            ans += max_right - waterArray[right]
        right -= 1

