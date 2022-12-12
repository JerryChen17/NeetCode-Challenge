class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        """
        compare nums == target
        if not go to (next index)
        
        define what is the next index (not 1, 2,... )
        """
        [L , R] = [0, len(nums) - 1]
        curMid = (R + L) // 2
        while target != nums[curMid]:
            if L >= R or L < 0 or R > len(nums) - 1:
                return -1
            if target > nums[curMid]:
                L = curMid + 1
                curMid = (R + L) // 2
                continue
            elif target < nums[curMid]:
                R = curMid - 1
                curMid = (R + L) // 2
                continue
            
        return curMid
test = Solution()
nums = [-1,0,3,5,9,12]
target = 9
print(test.search(nums, target))
            
