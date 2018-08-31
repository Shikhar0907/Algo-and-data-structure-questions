def matrix(mat):
    row = []
    col = []
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 1:
                row.append(i)
                col.append(j)

    for i in row:
        for j in range(len(mat[0])):
            mat[i][j] = 1
    for j in col:
        for i in range(len(mat)):
            mat[i][j] = 1
    print(mat)

def main():
    mat = [ [1, 0, 0, 1],
            [0, 0, 1, 0],
            [0, 0, 0, 0] ] 
    matrix(mat)

main()
