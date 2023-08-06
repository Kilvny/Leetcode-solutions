"""using greedy algorithm : on(n) T and o(1) space"""

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        r = 1 # the current steps we do have
        for n in nums:
            if r <= 0: return False # if r = 0 then we don't have any left jumps
            r = max(r-1, n) # we check if r is larger than n we keep standing at the same point and decrement one from the jump points we have, otherwise we stand at n
        return True
            