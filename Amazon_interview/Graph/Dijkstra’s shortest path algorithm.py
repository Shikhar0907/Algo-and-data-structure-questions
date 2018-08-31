class Graph():
    def __init__(self,vertices):
        self.v = vertices
        self.graph = [[0 for x in range(vertices)] for y in range(vertices)]


    def min_distance(self,dist,spt):
        min = 23423
        for v in range(self.v):
            if dist[v] < min and spt[v] == False:
                min = dist[v]
                min_index = v

        return(min_index)


    def print_solution(self,dist,parent):
        for node in range(self.v):
            print(node,dist[node],parent[node])

    def find_min_distance(self,src):
        max = 234534
        parent = [0] * self.v
        parent[0] = 0
        distance = [max] * self.v
        sptset = [False] *self.v
        distance[src] = 0

        for c in range(self.v):
            u = self.min_distance(distance,sptset)

            sptset[u] = True

            for v in range(self.v):
                if self.graph[u][v] > 0 and sptset[v] == False and distance[v] > distance[u] + self.graph[u][v]:
                    distance[v] = distance[u] + self.graph[u][v]
                    parent[v] = u


        self.print_solution(distance,parent)             
                

        
        


def main():
    root = Graph(9)
    root.graph = [ [0, 4, 0, 0, 0, 0, 0, 8, 0],
                   [4, 0, 8, 0, 0, 0, 0, 11, 0],
                   [0, 8, 0, 7, 0, 4, 0, 0, 2],
                   [0, 0, 7, 0, 9, 14, 0, 0, 0],
                   [0, 0, 0, 9, 0, 10, 0, 0, 0],
                   [0, 0, 4, 14, 10, 0, 2, 0, 0],
                   [0, 0, 0, 0, 0, 2, 0, 1, 6],
                   [8, 11, 0, 0, 0, 0, 1, 0, 7],
                   [0, 0, 2, 0, 0, 0, 6, 7, 0]
                 ]
    root.find_min_distance(0)

main()
