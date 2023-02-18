class Graph:
    def __init__(self,num_nodes,edges,directed=False):
        self.num_nodes = num_nodes
        self.data = [[] for _ in range(self.num_nodes)]
        self.weight = [[] for _ in range(self.num_nodes)]

        self.directed = directed
        for ele in edges:
            self.data[ele[0]].append(ele[1])
            self.weight[ele[0]].append(ele[2])

            if self.directed is False:
                self.data[ele[1]].append(ele[0])
                self.weight[ele[1]].append(ele[2])
            
    def __repr__(self):
       return "\n".join(["{} : {}".format(n,neighbour) for n,neighbour in enumerate(self.data)])

    def __str__(self):
        return self.__repr__()

def update_distance(graph,current,distance):
    neighbour = graph.data[current]
    weights = graph.weight[current]

    for i,node in enumerate(neighbour):
        weigh = weights[i]

        if (distance[current] + weigh) < distance[node]:
            distance[node] = distance[current] + weigh


def pick_next_node(distance,visited):
    min_dis = float('inf')
    min_node = None

    for node in range(len(distance)):
        if not visited[node] and distance[node]<min_dis:
            min_node = node
            min_dis = distance[node]

    return min_node

def shortPath(graph,start,goal):
    visited = [False] * (len(graph.data))
    distance = [[float('inf')] * (len(graph.data))]

    queue = []
    ind =0

    queue.append(start)
    distance[start] = 0
    visited[start] = True

    while ind<len(queue):
        current = queue[ind]

        update_distance(graph,current,distance)
        next_node=pick_next_node(distance,visited)

        if next_node is not None:
            visited[next_node] = True
            queue.append(next_node)
        ind+=1

    return distance[goal],distance
            

def main():
    num_nodes = 6
    edges = [(0, 1, 4), (0, 2, 2), (1, 2, 5), (1, 3, 10), (2, 4, 3), (4, 3, 4), (3, 5, 11)]
    gra = Graph(num_nodes, edges, directed=True)
    print(gra)
    print(gra.weight)
    v1,v2 = shortPath(gra,0,5)
    print(v1,v2)
    
if __name__ == "__main__":
    main()