class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        # prv answer was correct but it's run time is crazy Runtime
# 7236 ms. So we will try to optimize :) 
        

        # best solution
        myMap = {}

        for i, value in enumerate(nums):
            diff = target - value
            if diff in myMap:
                return [i, myMap[diff]]
            myMap[value] = i

        # lets start this first trial with a brute force technique 
        ans = []
        for j in range(len(nums)):
            for i in range(len(nums)):
                if (nums[i] + nums[j] == target) and (i != j):
                    ans.append(i)
                    ans.append(j)
                    return ans
        

        # we don't have to check the passed values in the array as we already checked it's pair with everyone after it already 

        ans = []
        for j in range(len(nums)):
            for i in range(j+1,len(nums)):
                if (nums[i] + nums[j] == target):
                    ans.append(i)
                    ans.append(j)
                    return ans 