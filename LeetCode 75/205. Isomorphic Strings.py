

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST,mapTS = {},{} # create two hashmaps

        for c1,c2 in zip(s,t): # as long as the two string[arrays] are the same length you can use zip method 
        # for i in range(len(s)) # or t it's same
        # c1,c2=s[i],s[t]
            if(c1 in mapST and mapST[c1] != c2 or c2 in mapTS and mapTS[c2] != c1):
                # condn simply is to make sure no character in one string it pointing to more than one char from the other...
                return False
            mapST[c1],mapTS[c2] = c2,c1 # same
            # mapST[c1] = c2
            # mapTS[c2] = c1
        return True
s = Solution()
print(s.isIsomorphic("يسثقضشر", "فودافون"))

solutionLink = 'https://www.youtube.com/watch?v=7yF-U1hLEqQ&ab_channel=NeetCode' # explained




