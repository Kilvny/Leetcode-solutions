class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        res = []
        for num in nums:
            res.append(nums[num])
        return res


c = Solution()
c.buildArray([5,0,1,2,3,4])