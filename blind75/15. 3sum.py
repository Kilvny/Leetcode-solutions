# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 






class RightSolution:
    def threeSum(self, nums:list):
        ans = []
        s = set()
        nums.sort()
        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1
            while j < k:
                cur = nums[i] + nums[j] + nums[k]
                if cur == 0:
                    s.add((nums[i],nums[j],nums[k]))
                    j +=1 # !!!! MOVE YOUR
                    k -=1 # !!!! P O I N T E R S
                elif cur < 0:
                    j +=1 # bcs the nums array are sorted remember?
                else:
                    k -=1
        ans = list(s)
        return ans
 
class Solution:
    def threeSum(self, nums:list):
        indexes = {}
        ans = []
        for i in range(len(nums)):
            # cur = nums[i]
            for j in range(i+1,len(nums)):
                # cur += nums[j]
                for k in range(j+1,len(nums)):
                    cur = nums[k] +nums[i] + nums[j]
                    if cur == 0 and sorted([nums[i],nums[j],nums[k]]) not in ans:
                        ans.append(sorted([nums[i],nums[j],nums[k]]))
        return ans
a = RightSolution()
print(a.threeSum([0,0,0,0,0,1,-1,1,-1,2,-2]))

# 308 / 312 testcases passed as Time Limit Exceeded:(((

# close solution but remains the distict part 


# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
 

# Constraints:

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105