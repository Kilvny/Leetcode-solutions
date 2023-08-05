class Solution: # correct solution
    def pivotIndex(self, nums: list[int]) -> int:
        totalsum = sum(nums)
        currentSum = 0
        i = 0
        while( i < len(nums)):
            
            currentSum+=nums[i]
            leftSum = currentSum - nums[i]
            rightSum = totalsum-currentSum
            
            if rightSum == leftSum:
                return(i)
               
            i+=1
               
        return(-1)



# x=[1,1,3,2,7,5,1,1]
# for i in range(len(x)):
#     if(sum(x[:i])==sum(x[i+1:])): 
#         print(i)
# print(False)


class WrongSolution:
    def pivotIndex(self, nums: list[int]) -> int:
        for i in range(len(nums)): # it was correct for 740/745 cases but time limit exceeded
            if(sum(nums[:i])==sum(nums[i+1:])): 
                return(i)
        return(-1)


if __name__=='__main__':
    x=Solution()
    print(x.pivotIndex(nums=[1,1,3,2,7,5,1,1]))


class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        totalsum = sum(nums)
        currentSum = 0
        
        for i in range(len(nums)):
            
            currentSum+=nums[i]
            leftSum = currentSum - nums[i]
            rightSum = totalsum-currentSum
            
            if rightSum == leftSum:
                return(i)
            
        return(-1)

"""
Runtime: 154 ms, faster than 95.67% of Python3 online submissions for Find Pivot Index.
Memory Usage: 15.2 MB, less than 48.58% of Python3 online submissions for Find Pivot Index."""