class Solution:
    def longestPalindrome(self, s: str) -> int:
        lettersMap = {}
        for char in s:
            if char not in lettersMap:
                lettersMap[char] = 1
            else:
                lettersMap[char] += 1 
            
        palindrome = 0
        oddchars = 0 
        
        if len(lettersMap) == 1: 
            return lettersMap[s[0]]
        
        for count in lettersMap.values():
            if count > 1:
                if count % 2 == 0:
                    palindrome += count
                else:
                    palindrome += ( count - 1 )
                    oddchars += 1
            else:
                oddchars += 1
        
        if oddchars > 0:
            palindrome += 1
            
        return palindrome