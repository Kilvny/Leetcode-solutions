class Solutionx:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:

        
        dp = [False] * (len(s) + 1)
        dp[0] = True # empty string is always breakable

        for i in range(1 , len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]


# sln = Solution()
# s = "leetcode"
# wordDict = ["leet","code"]
# print(sln.wordBreak(s, wordDict))
                



class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        # Initialize a dynamic programming table to keep track of subproblems
        dp = [False] * (len(s) + 1)
        dp[0] = True  # Empty string is always breakable
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                # Check if the substring from j to i is breakable
                print(f" s[j:i] : {s[j:i]} and dp[j]: {dp[j]}")
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[-1]  # Return the last element of dp, which represents the result

sln = Solutionx()
s = "leetcode"
wordDict = ["leet", "code"]
print(sln.wordBreak(s, wordDict))
