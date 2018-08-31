def lcs(x,y):
    L = [[0] *(len(y)+1) for i in range(len(x)+1)]

    for i in range(len(x)+1):
        for j in range(len(y)+1):
            if i ==0 or j == 0:
                L[i][j] = 0
            elif x[i-1] == y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j],L[i][j-1])

    return(L[i][j])


def main():
    x = "aggtab"
    y = "gxtxayb"
    print(lcs(x,y))


main()
    
