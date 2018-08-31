def Count_elements(mat,arr):
    for i in range(len(mat)):
        temp = {}

        for j in range(len(mat[0])):
            temp[mat[i][j]] = 1
        count = 0
        for j in range(len(arr)):
            if temp[arr[j]]:
                count += 1
        print("row {} = {}".format(i+1,count))
        
            




def main():
    mat = [[8,27,39,589,23],
            [23,34,589,12,45],
            [939,32,27,12,78],
            [23,349,48,21,32]]

    arr = [589,39,27]
    Count_elements(mat,arr)


main()
