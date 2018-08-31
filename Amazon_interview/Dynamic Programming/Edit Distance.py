def edit_distance(string1,string2):
    mat = [[0 for x in range(len(string2)+1)] for x in range(len(string1)+1)]

    for i in range(len(string1)+1):
        for j in range(len(string2)+1):
            if i == 0:
                mat[i][j] = j

            elif j == 0:
                mat[i][j] = i

            elif string1[i-1] == string2[j-1]:
                mat[i][j] = mat[i-1][j-1]

            elif string1[i-1] != string2[j-1]:
                mat[i][j] = min(mat[i-1][j],mat[i-1][j-1],mat[i][j-1])+1

                
    print(mat[i][j])
    
    for x in range(len(mat)):
        print(mat[x])




def main():
    string1 = "sunday"
    string2 = "saturday"
    edit_distance(string1,string2)

main()
