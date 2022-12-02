class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashMap = {}
        for i in range(len(nums)):
            numsStr = str(nums[i])
            if numsStr not in hashMap:
                hashMap[str(nums[i])] = nums[i]
                continue
            else:
                return True
        return False

nums = [1, 2, 3, 1]
test = Solution()
print(test.containsDuplicate(nums))