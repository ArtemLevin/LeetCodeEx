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


def volumeSearch(waterArray):
    volumeList = []
    maxValue = max(waterArray)
    rightArray = waterArray[waterArray.index(maxValue) + 1:]
    while len(rightArray) > 0:
        reduceVolumeValue = 0
        nextMax = max(rightArray)
        for i in range(rightArray.index(nextMax)):
            reduceVolumeValue += rightArray[i]
        volume = nextMax * (rightArray.index(nextMax)) - reduceVolumeValue
        print(nextMax, reduceVolumeValue, volume)
        volumeList.append(volume)
        rightArray = rightArray[rightArray.index(nextMax) + 1:]
    return volumeList


print(sum(volumeSearch(waterArray) + volumeSearch(waterArray[:waterArray.index(maxValue) + 1][::-1])))
