# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

"Note that you must do this in-place without making a copy of the array."


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        print(nums)
        j = 0
        for i in range(len(nums)):
            if (nums[i] != 0): # لو الرقم ده مش زيرو؟ هاتهولي في الأول وبعدين زودلي عداد ال جي عدة وعيد
                nums[j], nums[i] = nums[i], nums[j]
                j+=1
                print(f'nums is {nums}\n i is{i} j is {j}')

    

        return nums




array = [0,0,0,0,0,0,0,0,0,100,100,100,0,0,0,100,100]

nums = Solution()
nums1 = nums.moveZeroes(array)
print(nums1)






# leet code solution without print
"WRONG SOLUTION // 56 / 74 test cases passed."

class SolutionLeetCode:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.append(nums[i])
                nums.pop(i)
            if nums[i-1] == 0:
                nums.append(nums[i-1])
                nums.pop(i-1)



class AnotherWrongSolution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        print(nums)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == 0 and nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i] # because it exceeds time limit 

        # so the solution was instead of this I use another counter within the same loop...
