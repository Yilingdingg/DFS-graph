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

def Pre_t(root):
    print(root.value)
    if root.left!=None:
        Pre_t(root.left)
    if root.right!=None:
        Pre_t(root.right)

def Post_t(root):
    if root.left!=None:
        Post_t(root.left)
    if root.right!=None:
        Post_t(root.right)
    print(root.value)

def In_t(root):
    if root.left!=None:
        In_t(root.left)
    print(root.value)
    if root.right!=None:
        In_t(root.right)

graph_r = None
tree_r = None    

while True:
    print("\n DFS Graph Menu")
    print("1. Insert max value and edges")
    print("2. DFS graph")
    print("3. Preorder traversal")
    print("4. Postorder traversal")
    print("5. Inorder traversal")
    print("6. Exit")

    response=int(input("Enter your choice:"))

    if response==1:
        max_value=int(input("Enter the maximum value of node:"))
        graph_r=Graph(max_value)
        for i in range(max_value):
            edge_1=int(input("Enter the first value for the edge:"))
            edge_2=int(input("Enter the second value for the edge:"))
            graph_r.edge(edge_1,edge_2)

    elif response==2:
        if graph_r is None:
            print("First create a graph.")
        else:
            source_r=int(input("Choose a value for the source:"))
            result=graph_r.DFS(source_r)
            print("The result of the DFS graph is:", result)

    elif response in [3,4,5]:
            if response == 3:
                print("Pretarversal :")
                Pre_t(tree_r)
            elif response == 4:
                print("Posttraversal  :")
                Post_t(tree_r)
            elif response == 5:
                print("Intraversal :")
                In_t(tree_r)
            print()
    
    elif response==6:
        print("Exit program.")
        break

    else:
        print("Try again.")