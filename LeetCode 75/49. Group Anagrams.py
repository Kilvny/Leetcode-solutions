class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans = {}
        for w in strs:
            sorted_w = "".join(sorted(w))
            if sorted_w in ans:
                ans[sorted_w].append(w)
            else:
                ans[sorted_w] = [w]
        return list(ans.values())
