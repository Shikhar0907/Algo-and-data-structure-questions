def spiral_pattern(n):
    mat = [[0 for x in range(2*n-1)] for y in range(2*n-1)]
    top = 0
    left = 0
    right = len(mat[0])-1
    bottom = len(mat)-1
    while n > 0:
        for i in range(left,right+1):
            mat[top][i] = n
        for i in range(top,bottom+1):
            mat[i][right] = n
        for i in range(left,right+1):
            mat[bottom][i] = n
        for i in range(top,bottom+1):
            mat[i][left] = n
        top += 1
        bottom -=1
        left +=1
        right -= 1
        n -= 1
    
    for i in range(len(mat)):
        print(mat[i])
        



def main():
    n = 4
    spiral_pattern(n)

main()
