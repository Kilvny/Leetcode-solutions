#medium
class Solution:
    def minimumRounds(self, tasks: list ) -> int:
        ans = {}
        rounds = 0
        for i in range(len(tasks)):
            if tasks[i] not in ans:
                ans[tasks[i]] = 1 
            else:
                ans[tasks[i]] += 1
        for item, value in ans.items():
            if value < 2:
                return -1
            elif (value % 3 == 0):
                rounds += (value//3)
            elif (value % 3 != 0):
                rounds += ((value-1)//3) + 1
        return rounds 

s = Solution()
s.minimumRounds([2,2,3,3,2,4,4,4,4,4])