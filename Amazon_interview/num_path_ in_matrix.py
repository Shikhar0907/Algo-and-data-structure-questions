def num_path(r,c):
    count = [[0 for x in range(c)] for y in range(r)]
    
    for i in range(c):
        count[0][i] = 1
    for j in range(r):
        count[j][0] = 1

    for i in range(1,r):
        for j in range(c):
            count[i][j] = count[i-1][j] + count[i][j-1]
    return(count[r-1][c-1])


def main():
    r = 3
    c = 4
    print(num_path(r,c))


main()
