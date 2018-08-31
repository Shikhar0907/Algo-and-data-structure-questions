from collections import defaultdict
class Graph:
    def __init__(self,vertices):
        self.v = vertices
        self.graph = defaultdict(list)

    def add_edge(self,u,v):
        self.graph[u].append(v)


    def topological(self,v,visited,stack):
        visited[v] = True

        for i in self.graph[v]:
            if visited[i] == False:
                self.topological(i,visited,stack)
        print(v)
        stack.insert(0,v)

    def find_path(self):
        visited = [False] * self.v
        stack = []

        for i in range(self.v):
            if visited[i] == False:
                self.topological(i,visited,stack)
                
        print(stack)

def main():
    root = Graph(6)
    root.add_edge(5,2)
    root.add_edge(5,0)
    root.add_edge(4,0)
    root.add_edge(4,1)
    root.add_edge(2,3)
    root.add_edge(3,1)

    #print(root.graph)

    root.find_path()

main()
    
