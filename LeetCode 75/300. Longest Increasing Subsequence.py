from bisect import bisect_left


class Solution:
    @staticmethod
    def lengthOfLIS(nums: list[int]) -> int:
        
        def dfs(index, prv_val):
            if index >= len(nums):
                return 0
            
            take = 0
            if nums[index] > prv_val:
                take = 1 + dfs(index+1, nums[index])
            skip = dfs(index+1, prv_val)
            
            return max(take,skip)
        return dfs(0, float('-inf'))
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(Solution.lengthOfLIS(nums))  # Output: 4
# ! above is "time limit exceeded answer"

class Solutionx:
    @staticmethod
    def lengthOfLIS(nums: list[int]) -> int:
        sub = []
        for n in nums:
            if len(sub) == 0 or n > sub[-1]:
                sub.append(n)
            else:
                idx = bisect_left(sub, n)
                sub[idx] = n
        return len(sub)
            

nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(Solutionx.lengthOfLIS(nums))  # Output: 4
