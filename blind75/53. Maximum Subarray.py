class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # reset the total if it hits negative point 
        # choose the max of curSum and maxSub on each iteration
        maxSub = nums[0]
        curSum = 0
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub