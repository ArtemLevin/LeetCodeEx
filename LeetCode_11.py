# You are given an integer array height of length n. There are n vertical
# lines drawn such that the two endpoints of the ith line are (i, 0)
# and (i, height[i]).
# Find two lines that together with the x-axis form a container,
# such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

import random

n = int(input("Enter the number of lines ---> "))

waterArray = [random.randint(1, 10) for i in range(n)]
print (waterArray)
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

enumWaterArrayList = list(enumerate(waterArray))
sortedEnumerateWaterArrayList = sorted(enumWaterArrayList, key=lambda x: x[1], reverse=True)
print(sortedEnumerateWaterArrayList)
maxVolume = 0
while len(sortedEnumerateWaterArrayList) > 0:
    i = 0
    while i < len(sortedEnumerateWaterArrayList):
        waterVolume = sortedEnumerateWaterArrayList[i][1]*abs(sortedEnumerateWaterArrayList[0][0]-sortedEnumerateWaterArrayList[i][0])
        if waterVolume > maxVolume:
            maxVolume = waterVolume
            print(maxVolume, waterVolume)
        i += 1
    sortedEnumerateWaterArrayList.pop(0)
print(maxVolume)