# LeetCode724_FindPivotIndex.py
# Ad
# Given an array of integers nums, write a method that returns the "pivot" index of this array. 
# We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index. 
# If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index. 

# solution ---------------------------------------------------------------------

class Solution:
    def pivotIndex(self, nums):
        leftSum, rightSum = 0, sum(nums)
        for index in range(0, len(nums)):
            rightSum -= nums[index]
            if leftSum == rightSum:
                return index
            leftSum += nums[index]
        return -1

# test -------------------------------------------------------------------------