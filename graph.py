# Graph using adjacency list
class graphL:
    def __init__(self,num_node,edges):
        self.num_node = num_node
        self.edges = [[] for _ in range(num_node)]

        for n,v in edges:
            self.edges[n].append(v)
            self.edges[v].append(n)

    def __repr__(self):
       return "\n".join(["{} : {}".format(n,neighbour) for n,neighbour in enumerate(self.edges)])

    def __str__(self):
        return self.__repr__()

    
    # Breadth first Search
    def bfs(self,root):
        queue = []
        visited = [False] * (len(self.edges))
        distance = [0] * (len(self.edges))
        parent = [None] * (len(self.edges))

        queue.append(root)
        visited[root] = True
        ind = 0

        while ind<len(self.edges):
            
            cur = queue[ind]
            ind+=1

            for node in self.edges[cur]:
                if visited[node] is False:
                    visited[node] = True
                    distance[node] = 1 + distance[cur]
                    parent[node] = cur
                    queue.append(node)

        return queue,distance,parent



    def dfs(self,root):
        stack = []
        visited = [False] * (len(self.edges))
        result = []

        stack.append(root)

        while len(stack)>0:
            cur = stack.pop()
            
            if visited[cur] is False:
                visited[cur] = True
                result.append(cur)
                for node in self.edges[cur]:
                    if visited[node] is False:
                        stack.append(node)
        return result



    



def main():
    num_node = 5
    edges = [(0,1),(0,4),(1,2),(1,3),(1,4),(2,3),(3,4)]
    obj=graphL(num_node,edges)
    val = obj.dfs(3)
    print(val)
    #val4 = obj.dfs(3)
    #print(val4)
    #print(obj)

if __name__ == "__main__":
    main()