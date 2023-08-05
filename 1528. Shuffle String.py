class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        shuffled = [0] * (len(indices))
        for i in range(len(indices)):
            shuffled[indices[i]] = s[i]
        return "".join(shuffled)
    

s = Solution()
print(s.restoreString(s="codeleet", indices=[4,5,6,7,0,2,1,3]))