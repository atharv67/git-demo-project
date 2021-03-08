from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        print(u,v)
        self.graph[u].append(v)
    def display_graph(self):
        for i in self.graph:
            print(i,": ",end=" ")
            for j in self.graph[i]:
                print(j,"->",end="")
            print()
def dfsUtil(graph,u,visited,result,final):
    result.append(u)
    visited.append(u)
    if u==final:
        print(result,u)
        return
    # print(visited,u,graph[u])
    for i in graph[u]:
        if i not in visited:
            dfsUtil(graph,i,visited,result,final)
def dfs(graph,u,final):
    result=[]
    visited=[]
    dfsUtil(graph,u,visited,result,final)
    # print(result)
def bfs(graph,u,f):
    result=[]
    visited=[]
    queue=[]
    queue.append(u)
    visited.append(u)
    print(visited)
    while len(queue)!=0:
        # print('queue',queue)
        node=queue.pop(0)
        result.append(node)
        if node==f:
            print(node,result)
            return
        # print(node,visited)
        for i in graph[node]:
            if i not in visited: 
                queue.append(i) 
                visited.append(i)
    print("bfs=",result)
def dfsUtil(graph,u,visited,result,final,depth):
    result.append(u)
    visited.append(u)
    if u==final:
        print(result,u)
        return
    if depth==0:
        print('Not found')
        return
    
    # print(visited,u,graph[u])
    for i in graph[u]:
        if i not in visited:
            dfsUtil(graph,i,visited,result,final,depth-1)
def dfs(graph,u,final,depth):
    result=[]
    visited=[]
    dfsUtil(graph,u,visited,result,final,depth)

def djikstra(graph,u):
    distances=[sys.maxsize]*len(graph)
    visited=[0]*len(graph)
    distances[u]=0
    queue=[]
    queue.append(u)
    while len(queue)!=0:
        i=queue.pop(0)
        if visited[i]==0:
            for j in graph[i]:
                queue.append(j)
                if distances[i]>distances[u]+1:
                    distances[i]=distances[u]+1
    print(distances)
if __name__=="__main__":
    g=Graph()
    g.addEdge('A', 'B')
    g.addEdge('A', 'E')
    g.addEdge('B', 'A')
    g.addEdge('B', 'C')
    g.addEdge('B', 'F')
    g.addEdge('C', 'B')
    g.addEdge('C', 'D')
    g.addEdge('C', 'G')
    g.addEdge('D', 'C')
    g.addEdge('D', 'H')
    g.addEdge('E', 'A')
    g.addEdge('E', 'F')
    g.addEdge('E', 'I')
    g.addEdge('F', 'B')
    g.addEdge('F', 'E')
    g.addEdge('F', 'G')
    g.addEdge('F', 'J')
    g.addEdge('G', 'C')
    g.addEdge('G', 'F')
    g.addEdge('G', 'H')
    g.addEdge('G', 'K')
    g.addEdge('H', 'D')
    g.addEdge('H', 'G')
    g.addEdge('H', 'L')
    g.addEdge('I', 'E')
    g.addEdge('I', 'J')
    g.addEdge('I', 'M')
    g.addEdge('J', 'F')
    g.addEdge('J', 'I')
    g.addEdge('J', 'K')
    g.addEdge('J', 'N')
    g.addEdge('K', 'O')
    g.addEdge('K', 'L')
    g.addEdge('K', 'J')
    g.addEdge('K', 'G')
    g.addEdge('L', 'H')
    g.addEdge('L', 'K')
    g.addEdge('L', 'P')
    g.addEdge('M', 'I')
    g.addEdge('M', 'N')
    g.addEdge('N', 'M')
    g.addEdge('N', 'J')
    g.addEdge('N', 'O')
    g.addEdge('O', 'N')
    g.addEdge('O', 'K')
    g.addEdge('O', 'P')
    g.addEdge('P', 'O')
    g.addEdge('P', 'L') 
    g.display_graph() 
    bfs(g.graph,'A','P')
    dfs(g.graph,'A','P')
    
    