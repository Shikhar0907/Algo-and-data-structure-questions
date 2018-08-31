def maze(mat):
    for i in range(len(mat)):
        if mat[i][0] == 0:
            mat[i][0] = 1
        else:
            break
    for j in range(1,len(mat[0])):
        if mat[0][j] == 0:
            mat[0][j] = 1
        else:
            break

    for i in range(1,len(mat)):
        for j in range(1,len(mat[0])):
            if mat[i][j] == -1:
                continue
            if mat[i-1][j] > 0:
                mat[i][j] = mat[i][j] + mat[i-1][j]

            if mat[i][j-1] > 0:
                mat[i][j] = mat[i][j] + mat[i][j-1]



    print(mat)




def main():
    mat =[[0,0,0,0],
          [0,-1,0,0],
          [-1,0,0,0],
          [0,0,0,0]];

    maze(mat)


main()
