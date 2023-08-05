# brute force (TIME LIMIT )

class BruteForceSolution:
    def maxArea(self, height: List[int]) -> int:
        alt = height[0]
        water = 0
        for i in range(len(height)):
            distance = 0
            for j in range(i+1, len(height)):
                distance +=1
                cur = distance * (min(height[i],height[j]))
                water = max(water, cur)
        return water 


# have two pointers (sliding window) and check the one with less height and shift it 

class Solution:
    def maxArea(self, height: List[int]) -> int:
        water = 0
        l, r = 0, len(height) - 1

        while l < r:
            cur = (r - l) * min(height[l], height[r])
            water = max(water, cur)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
    return water
on = """
    Runtime
768 ms
Beats
57.42%
Memory
27.4 MB
Beats
84.86%"""

