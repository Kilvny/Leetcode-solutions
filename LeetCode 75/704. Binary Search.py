class Solution:
    def search(self, nums: list[int], target: int) -> int:
        mini,maxi = 0,len(nums-1)
        while( mini <= maxi ): # you must do the equal sign ( suppose the array is [5] and the target is 5 ! )
            midpoint = (mini+maxi) // 2
            if nums[midpoint] > target:
                maxi = midpoint - 1
            elif nums[midpoint] < target:
                mini = midpoint + 1
            elif target == nums[midpoint]:
                return midpoint
        return None # will get here if element is not found