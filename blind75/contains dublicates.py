class Solution:
    def contains_dub(self, list:list):
        if (len(set(list)) != len(list)):
            return True
        return False



a = Solution()
print(a.contains_dub([1,0,2]))