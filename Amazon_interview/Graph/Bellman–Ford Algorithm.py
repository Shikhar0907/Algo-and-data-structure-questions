class Graph:
    def __init__(self,vertices):
        self.v = vertices
        self.graph = []

    def add_edge(self,u,v,w):
        self.graph.append([u,v,w])


    def Bellman_ford(self,src):
        INF = 999999999
        dist = [INF] * self.v
        dist[src] = 0

        for i in range(self.v-1):
            for u,v,w in self.graph:
                if dist[u] != INF and dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w


        print(dist)



def main():
    root = Graph(5)
    root.add_edge(0, 1, -1)
    root.add_edge(0, 2, 4)
    root.add_edge(1, 2, 3)
    root.add_edge(1, 3, 2)
    root.add_edge(1, 4, 2)
    root.add_edge(3, 2, 5)
    root.add_edge(3, 1, 1)
    root.add_edge(4, 3, -3)

    #print(root.graph)

    root.Bellman_ford(0)


main()
