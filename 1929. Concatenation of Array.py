class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        nums = nums+nums
        return nums



def getConcatenation(nums:list[int]):
        nums = nums+nums
        return nums
arr=[1,2,3,4]

print(getConcatenation(arr))