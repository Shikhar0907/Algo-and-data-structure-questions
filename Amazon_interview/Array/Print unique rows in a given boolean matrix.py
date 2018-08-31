def matrix(mat):
    temp = []
    for item in mat:
        if item not in temp:
            temp.append(item)
        else:
            pass
    print(temp)




def main():
    mat = [ [0, 1, 0, 0, 1],
            [1, 0, 1, 1, 0],
            [0, 1, 0, 0, 1],
            [1, 0, 1, 0, 0] ]
    matrix(mat)

    
main()
