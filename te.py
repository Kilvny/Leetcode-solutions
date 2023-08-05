# x = '00000000000000000000000000001011'

# count = 0
# for char in x:
#     if char == '1':
#         count +=1
# print(count)


class Solution:
    def hammingWeight(self, n: int) -> int:
        x = str(bin(n))
        count = 0 
        for char in x:
            if char == '1':
                count += 1
        
        print(count)
        return count
s = Solution()

s.hammingWeight(1500)


"""
Runtime: 66 ms, faster than 24.62% of Python3 online submissions for Number of 1 Bits.
Memory Usage: 14 MB, less than 7.85% of Python3 online submissions for Number of 1 Bits."""


class AnotherSolution:
    def hammingWeight(self, n: int) -> int:    
        return str(bin(n)).count("1")

"""
Runtime: 56 ms, faster than 57.29% of Python3 online submissions for Number of 1 Bits.
Memory Usage: 13.8 MB, less than 49.85% of Python3 online submissions for Number of 1 Bits."""



"""
class Solution:
    def hammingWeight(self, n: int) -> int: 
        # O(n) runtime, O(1) space
        ans = 0
        while n:
            n &= (n-1) # removes the rightmost bit
            ans += 1
        return ans
        
        # O(n) runtime, O(1) space
        ans = 0
        while (n != 0):
            ans = ans + (n & 1) # removes the rightmost bit
            n = n >> 1
        return ans
    
        return str(bin(n)).count("1")"""