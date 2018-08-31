def find_position(mat,target):
    row = 0
    col = len(mat[0])-1
    while row < len(mat) and col > -1:
        cur_point = mat[row][col]
        if cur_point < target:
            row += 1
        elif cur_point > target:
            col -= 1
        elif cur_point == target:
            return(True)

    return(False)

def main():
    mat = [[1,3, 5, 7, 9],
          [11,13,15,16,20],
          [21,22,23,24,25],
          [30,32,35,40,45],]
    target = 23
    print(find_position(mat,target))

main()
