class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:  
        i = 0
        newArr = [] 
        while (i<len(nums)):
            newArr.append(sum(nums[:i+1]))
            i+=1

        return newArr

# another solution by another user : 
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:

        index=0
        
        for number in range(len(nums)-1):
            
            nums[index],nums[index+1] = nums[index],nums[index]+nums[index+1]
            index+=1
        return nums
