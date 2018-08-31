class Graph():
    def __init__(self,vertices):
        self.v = vertices
        self.graph = [[0 for x in range(vertices)] for y in range(vertices)]

    def print_graph(self,parent):
        for i in range(1,self.v):
            print(parent[i] ,i,self.graph[i][parent[i]])
            

    def min_distance(self,dist,visited):

        min = 23434
        for v in range(self.v):
            if dist[v] < min and visited[v] == False:
                min = dist[v]
                min_index = v
        return(min_index)
    
    def prims(self):
        max  = 234564
        dist = [max] * self.v
        dist[0] = 0
        visited = [False] * self.v
        parent = [0] *self.v
        parent[0] = 0

        for c in range(self.v):
            u = self.min_distance(dist,visited)

            dist[u] = True

            for v in range(self.v):
                if self.graph[u][v] > 0 and visited[v] == False and dist[v] > self.graph[u][v]:
                    dist[v] = self.graph[u][v]
                    parent[v] = u

        self.print_graph(parent)            


        

def main():
    root = Graph(5)
    root.graph = [ [0, 2, 0, 6, 0],
                 [2, 0, 3, 8, 5],
                 [0, 3, 0, 0, 7],
                 [6, 8, 0, 0, 9],
                 [0, 5, 7, 9, 0],
                   ]



    root.prims()


main()
