class SolutionExplained:
    def minTime(self, n: int, edges: list, hasApple: list[bool]) -> int:
        # first we create a hashtable of adjacency(neighbours) list for each node 
        adj = { i:[] for i in range(n)}
        # fill the hashtable with neighbours
        for par, chi in edges:
            adj[par].append(chi)
            adj[chi].append(par)
        
        # our dfs function to vist the nodes with the current node and it's parent passed 
        def dfs(cur_node, par):
            time = 0 # to keep track this what we will return

            # we will go through 
            for chi in adj[cur_node]:
                # because we have the parent as a neighbour we don't want to revisit it and get stuck in an infinite loop
                if chi == par:
                    continue 
                # if the child is unique and not a parent then we want to check on it's sons( subtree of the child and add that childtime to ourtime)
                childTime = dfs(chi, cur_node)
                if childTime or hasApple[chi]:
                    time += childTime + 2 
            return time
        return dfs(0, -1) # we pass -1 as initial value of parent cause node 0 doesn't have a parent:) 


class Solution:
    def minTime(self, n: int, edges: list[list[int]], hasApple: list[bool]) -> int:
        # first we create a hashtable of adjacency(neighbours) list for each node 
        adj = { i:[] for i in range(n)}
        # fill the hashtable with neighbours
        for par, chi in edges:
            adj[par].append(chi)
            adj[chi].append(par)
        
        # our dfs function to vist the nodes with the current node and it's parent passed 
        def dfs(cur_node, par):
            time = 0 # to keep track this what we will return

            for chi in adj[cur_node]:
                if chi == par:
                    continue 
                childTime = dfs(chi, cur_node)
                if childTime or hasApple[chi]:
                    time += childTime + 2 
            return time
        return dfs(0, -1) # we pass -1 as initial value of parent cause node 0 doesn't have a parent:) 
