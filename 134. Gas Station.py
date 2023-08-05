class Solution:
    def canCompleteCircuit(self, gas: list, cost: list) -> int:
        # there is no solution
        if sum(gas) < sum(cost):
            return -1
        # but if we passed this check, there is solution
        startAt , tank = [] , 0

        # create the diff list :
        diff = []
        for i,j in zip(gas,cost):
            diff.append(i-j)

        for i in range(len(diff)):
            tank += diff[i]
            if tank < 0:
                tank = 0
                continue
            startAt.append(i)
        return startAt[0]


gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
s = Solution()
print(s.canCompleteCircuit(gas,cost))