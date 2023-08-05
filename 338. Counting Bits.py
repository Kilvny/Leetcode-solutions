class Solution:
    def countBits(self, n: int) -> list:
        ones,res = [],[]
        for i in range(n+1):
            binary = bin(i)[2:]
            ones = [1 if number == '1' else 0 for number in binary]
            res.append(sum(ones))
        return res

# x=6
# ones = []
# binary = bin(x)[2:]
# ones = [1 if number == '1' else 0 for number in binary ]
# print(sum(ones))

s = Solution()
s.countBits(5)