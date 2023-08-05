# class Solution:
#     def trap(self, height: list[int]) -> int:
#         trap = 0 
#         for i in range(1,len(height)):
#             if height[i] < height[i-1]:
#                  trap += (height[i-1] - height[i])
#                  height[i] = height[i-1] 
#         return trap

# s = Solution()
# s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
"""
HARD

"""

def trap(self, height):
    waterLevel = []
    left = 0
    for h in height:
        left = max(left, h) 
        waterLevel += [left] # over-fill it to left max height
    right = 0
    for i, h in reversed(list(enumerate(height))):
        right = max(right, h)
        waterLevel[i] = min(waterLevel[i], right) - h # drain to the right height
    return sum(waterLevel)