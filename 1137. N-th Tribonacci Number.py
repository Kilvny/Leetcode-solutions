class Solution:
    def tribonacci(self, n: int) -> int:
        nums = [0] * (n+1)
        if(n > 2):
            nums[1] = 1
            nums[2] = 1
        for i in range(3,n+1):
            nums[i] = sum(nums[i-3:i+1])
        print(nums)
        return nums[n]


c = Solution()
c.tribonacci(6)