class Solution:
    def minDeletionSize(self, strs: list) -> int:
        count = 0
        j = 0
        while(j<len(strs[0])):
            issorted = ''
            for i in range(len(strs)):
                issorted += strs[i][j]
            if((''.join(sorted(issorted))!=issorted)):
                count +=1
            j += 1

        return count


x = 'abc'
y = 'cao'
s = Solution()
print(s.minDeletionSize([x,y]))
