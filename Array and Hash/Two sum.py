class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        #iterating through nums and use point 1 and target - point 1 to find point 2
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == (target - nums[i]):
                    return [i, j]
        """

        #using hash map to save the object in the nums but value is the index

        prevNums = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in prevNums:
                return [prevNums[diff], i]

            prevNums[n] = i  