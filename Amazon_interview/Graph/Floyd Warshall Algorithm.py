v = 4
INF = 999999

def floydwaterfall(graph):
     dist = graph
     for k in range(v):
         for i in range(v):
             for j in range(v):
                 dist[i][j] = min(dist[i][j],(dist[i][k]+dist[k][j]))
     print(dist)




def main():
   graph =  [[0,5,INF,10],
             [INF,0,3,INF],
             [INF, INF, 0,   1],
             [INF, INF, INF, 0]
            ]
   floydwaterfall(graph)

main()
    
