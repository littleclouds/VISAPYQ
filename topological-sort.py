'''
Given an adjacency list for a Directed Acyclic Graph (DAG) where adj[u] contains a list of all vertices v such that there exists a directed edge u -> v. Return topological sort for the given graph.

Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge u -> v, vertex u comes before v in the ordering.
Note: As there are multiple Topological orders possible, you may return any of them. If your returned Topological sort is correct then the output will be 1 else 0.
Constraints:
2  ≤  V  ≤  103
1  ≤  E  ≤  (V * (V - 1)) / 2
'''

from queue import Queue
class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topologicalSort(self,adj):
        q=Queue()
        n=len(adj)
        vis=[]
        st=[]
        ind=[]
        for i in range(n):
            vis.append(0)
            ind.append(0)
        for i in range(n):
            for j in adj[i]:
                ind[j]+=1 
        for i in range(n):
            if ind[i]==0:
                q.put(i)
                vis[i]=1
        ans=[]
        while not q.empty():
            node=q.get()
            ans.append(node)
            for j in adj[node]:
                ind[j]-=1 
                if ind[j]==0 and vis[j]==0:
                    q.put(j)
                    vis[j]=1 
        return ans
