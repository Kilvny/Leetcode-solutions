class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        for j in range(len(t)):
            if(len(s)<1): # if s string is empty string it's sub of the 2nd
                return True
            
            if(s[i] == t[j]): # if char found only if then i+1 to check next char and j maintain the order anyways
                
                i+=1
            
            if i == len(s): # all i is found 
            
                return i == len(s)

        return i == len(s) # will get here only if not all i is found 
    

# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         i, j = 0, 0
#         while i < len(s) and j < len(t):
#             if s[i] == t[j]:
#                 i+=1
#             j+=1

#         return i == len(s)



s = Solution()
print(s.isSubsequence('axe','ahbgdc')
)        
        
        
        
        
        
#         Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

#         Input: s = "axc", t = "ahbgdc"
# Output: false



# check subseq?

def checksubseq(s:str,t:str):
    i=0
    for j in range(len(t)):
        print(f's[i] : {s[i]} and t[j] : {t[j]}')
        if(s[i] == t[j]):
            i+=1
        if i == len(s):
            return i == len(s)

    return i == len(s)

print(checksubseq('123','1000000000200000003'))