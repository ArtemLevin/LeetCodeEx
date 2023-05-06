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

newWaterArray = sorted(waterArray, reverse=True)
print(newWaterArray)
i = 0
waterVolumeArray = []
while i < len(newWaterArray):
    waterVolumeArray.append(i*(newWaterArray[i]))
    print(waterVolumeArray)
    i += 1
print(waterVolumeArray)
maxVolume = max(waterVolumeArray)
print(maxVolume)