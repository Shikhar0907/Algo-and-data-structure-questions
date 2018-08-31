def Max_product(arr):
    max_num = arr[0]
    max_second = arr[1]

    for i in range(2,len(arr)):
        if max_num < arr[i]:
            max_second = max_num
            max_num = arr[i]
    print(max_second,max_num)        
            
def main():
    arr = [1,4,3,6,7,0]
    Max_product(arr)

main()
 
