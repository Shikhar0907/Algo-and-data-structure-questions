def find_max_product(arr):
    max_num = -2342342
    second_max = -234242544

    for item in arr:
        if item > max_num:
            second_max = max_num
            max_num = item
            

    return(second_max,max_num)



def main():
    arr = [1,4,3,6,7,0]
    print(find_max_product(arr))

main()
