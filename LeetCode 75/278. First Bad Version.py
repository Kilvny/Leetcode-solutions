# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low,high = 0,n
        while (low <= high):
            middle_point = (low + high) // 2
            if(isBadVersion(middle_point)):
                if(isBadVersion(middle_point-1)==False):
                    return middle_point
                high = middle_point - 1 
            else:
                low = middle_point + 1 