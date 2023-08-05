class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        self.graph = graph
        self.path = []
        self.res = []
        self.n = len(graph)
        
        
        self.dfs(0)
        return self.res

    def dfs(self, v: int) -> None:
        """
        :param v: the current visited node 
        """
        self.path.append(v)
        if v == self.n - 1: # we have reached the edge 'Targer'
            self.res.append(self.path[:])
        else:
            for n in self.graph[v]: # traverse the current node nighbours 
                self.dfs(n)
        self.path.pop() # remove the last node from current path to allow backtracking other nighbours

s = Solution()
print(s.allPathsSourceTarget(([[1,2,3],[2],[3],[]])))