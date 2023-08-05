class Solution:
    def findComplement(self, num: int) -> int:
        comp = ''
        for n in str(bin(num)[2:]):
            if n == '0':
                comp+='1'
            else:
                comp+=('0')
        return int(comp,2)


s = Solution()
print(s.findComplement(5))

