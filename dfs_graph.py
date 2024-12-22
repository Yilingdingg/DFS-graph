class Graph:
    def __init__(self, n):
        self.n=n
        self.adj=[[]*n for i in range(n)]
        print(self.adj)
        
    def edge(self,x,y):
        self.adj[x-1].append(y-1)
        self.adj[y-1].append(x-1)
        print(self.adj)
    
    def DFS_util(self, src, visited, res):
        res.append(src)
        visited[src]=True
        for node in self.adj[src]:
            if visited[node]==False:
                self.DFS_util(node,visited,res)   

    def DFS(self, src):
        visited=[False]*self.n
        res=[]
        self.DFS_util(src,visited,res)
        return res
    
graph1=Graph(6)
graph1.edge(1,2)
graph1.edge(2,3)
graph1.edge(3,1)
graph1.edge(3,4)
graph1.edge(4,5)
graph1.edge(4,6)

result=graph1.DFS(0)
print("The result of the DFS graph is:", result)