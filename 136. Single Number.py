class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        map = {} 
        for i in range(len(nums)):
            if nums[i] in map:
                map[nums[i]] = 0
            else:
                map[nums[i]] = 1
        result = dict((val,key) for key,val in map.items()).get(1)
        # here I created a new dict and vice versa for key and value bcs get method search for keys
        # so i will have my OLD key as my NEW value and OLD value and my NEW key
        # this way for example if dict {40:1,
        #                               20,0,
        #                               30,0} 
        # will change the 1 and 0 as keys and then will get you the value of 40 by searching for the value you already know which is now A KEY 
        # NOTE : THIS WHOLE METHOD WAS USED BECAUSE I KNOW THE VALUE AND I WANT TO GET THE KEY
        return result

"""
Runtime: 300 ms, faster than 43.55% of Python3 online submissions for Single Number.
Memory Usage: 16.6 MB, less than 83.77% of Python3 online submissions for Single Number.
"""


s = Solution()
print(s.singleNumber([4,1,2,1,2]))