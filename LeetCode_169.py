# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋
# times. You may assume that the majority element always exists in the array.
from collections import Counter


def majorityElement(nums):
    return sorted(Counter(nums).items(), key = lambda x: x[1], reverse =True)[0][0]

print(majorityElement([1,1,1,2,3,4,4,4, 5, 5,5,5]))

