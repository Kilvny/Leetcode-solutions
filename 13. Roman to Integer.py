class Solution:
    def romanToInt(self, s: str) -> int:
        romToint = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
            'IV' : 4,
            'IX' : 9,
            'XL' : 40,
            'XC' : 90,
            'CD' : 400,
            'CM' : 900
        }

        converted = 0

        for i in range(len(s)):
            if s[i] == 'M':
                if i > 0 and s[i-1] == 'C':
                    converted -= romToint['C']
                    converted += romToint['CM']
                else: 
                    converted += romToint[s[i]]                                 
            elif s[i] == 'D':
                if i > 0 and s[i-1] == 'C':
                    converted -= romToint['C']
                    converted += romToint['CD']
                else: 
                    converted += romToint[s[i]]   
            elif s[i] == 'C':
                if i > 0 and s[i-1] == 'X':
                    converted -= romToint['X']
                    converted += romToint['XC']
                else: 
                    converted += romToint[s[i]]   
            elif s[i] == 'L':
                if i > 0 and s[i-1] == 'X':
                    converted -= romToint['X']
                    converted += romToint['XL']
                else: 
                    converted += romToint[s[i]]  
            elif s[i] == 'X':
                if i > 0 and s[i-1] == 'I':
                    converted -= romToint['I']
                    converted += romToint['IX']
                else: 
                    converted += romToint[s[i]]                 
            elif s[i] == 'V':
                if i > 0 and s[i-1] == 'I':
                    converted += romToint['IV']
                    converted -= romToint['I']
                else:
                    converted += romToint[s[i]]                 
            elif s[i] == 'I':
                converted += romToint[s[i]]                 
        return converted



o = Solution()
print(o.romanToInt('MCMXCIV'))


# Accepted from the first time :)
# that's the normal now tehe..

""" 
Runtime: 59 ms, faster than 83.39% of Python3 online submissions for Roman to Integer.
Memory Usage: 14 MB, less than 30.67% of Python3 online submissions for Roman to Integer.

"""



class IQ200SolutionByLeetcoder:
    def romanToInt(self, s: str) -> int:
        roman_to_integer = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
        return sum(map(lambda x: roman_to_integer[x], s)) 

        # the lambda function takes the x which is the Char from s and map iterates over the string and then sum gets the final result!