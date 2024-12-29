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
    
    def BFS(self, src):
            visited=[False]*self.n
            distance=[-1]*self.n
            res=[]
            queue=[]
            queue.append(src)
            visited[src]=True
            distance[src]=0
            while len(queue) > 0:
                s=queue.pop(0)
                res.append(s)
                for item in self.adj[s]:
                    if visited[item]==False:
                        queue.append(item)
                        visited[item]=True
                        distance[item]=distance[s]+1
            return distance

while True:
    print("\n DFS Graph Menu")
    print("1. Insert max value and edges")
    print("2. DFS graph")
    print("3. BFS graph")
    print("4. Exit")

    response=int(input("Enter your choice:"))

    if response==1:
        max_value=int(input("Enter the maximum value of node:"))
        graph_r=Graph(max_value)
        for i in range(max_value):
            edge_1=int(input("Enter the first value for the edge:"))
            edge_2=int(input("Enter the second value for the edge:"))
            graph_r.edge(edge_1,edge_2)

    elif response==2:
            source_d=int(input("Choose a value for the source:"))
            result=graph_r.DFS(source_d)
            print("The result of the DFS graph is:", result)

    elif response==3:
            source_b=int(input("Choose a value for the source:"))
            result=graph_r.BFS(source_b)
            print("The result of the BFS graph is:", result)        

    elif response==4:
        print("Exit program.")
        break

    else:
        print("Try again.")