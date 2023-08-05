class Solution:
    def minCost(self, colors: str, neededTime: list) -> int:
        totalT = cur_time = 0
        for i in range(len(colors)):
            if i > 0 and colors[i] != colors[i-1]:
                cur_time = 0
            
            totalT += min(cur_time,neededTime[i])
            cur_time = max(cur_time,neededTime[i])
            print(f"total time :{totalT} cur = {cur_time} and i: {i}")
        return totalT

s = Solution()
print(s.minCost("aaabbbabbbb",
[3,5,10,7,5,3,5,5,4,8,1]))

"""
Runtime: 1221 ms, faster than 89.92% of Python3 online submissions for Minimum Time to Make Rope Colorful.
Memory Usage: 24.9 MB, less than 75.42% of Python3 online submissions for Minimum Time to Make Rope Colorful."""