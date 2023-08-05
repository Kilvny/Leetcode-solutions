"""
Related Topics
@Array
@Hash Table
@Graph

"""

## my wrong solution 
class WrongSolution:
    def findJudge(self, n: int, trust: list) -> int:
        # create a hashtable 
        hashtable = { i+1: [] for i in range(n)}
        if len(trust) < 1 :
            return n
        prv = trust[0][1]
        for i in range(len(trust)):
            hashtable[i+1] = trust[i]
            if prv != trust[i][1]:
                return -1

        print(hashtable)
        flag = 0
        judge = 0
        for key,value in hashtable.items():
            if value == []:
                 judge = key
                 flag += 1
        if flag == 1:
            return judge
        return -1

class CorrectSolution:
    def findJudge(self, n: int, trust:list):
        trusted = [0] * (n+1) # create a graph counter to keep track of trust count for each number
        print(trusted) # zeros
        for a,b in trust:
            trusted[a] -= 1 # he who trusts someone can never satisfy n-1 and therefore can never be the judge
            trusted[b] += 1 # judge probability increases
        print(trusted)
        for i in range(1,n+1):
            if trusted[i] == n-1: # n-1 because this means everybody except him trust him :) 
                return i
        # else
        return -1
    
s = CorrectSolution()
s.findJudge(4,[[1,3],[1,4],[2,3],[2,4],[4,3]])


class TrainingReSolution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        judgescore = [0] * (n+1)
        for i,j in trust:
            judgescore[i] -= 1
            judgescore[j] += 1
        for i in range(len(judgescore)):
            if (judgescore[i] == n-1):
                return i 
        return -1
me = TrainingReSolution()
print(me.findJudge(4,[[1,3],[1,4],[2,3],[2,4],[4,3]]))