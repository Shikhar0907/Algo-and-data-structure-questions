def path(mat):
    C =3
    R = 3
    cost = [[0 for x in range(C)] for x in range(R)]
    cost[0][0] = mat[0][0]
    for i in range(1,len(mat)):
        cost[i][0] = cost[i-1][0] + mat[i][0]
        

    for i in range(1,len(mat[0])):
         cost[0][i] = cost[0][i-1] + mat[0][i]


    for i in range(1,len(mat)):
        for j in range(1,len(mat[0])):
            cost[i][j] = min(cost[i-1][j-1],cost[i-1][j],cost[i][j-1]) + mat[i][j]
    
    print(cost)     
        



def main():
    mat= [  [1, 2, 3],
            [4, 8, 2],
            [1, 5, 3] ]

    path(mat)


main()
