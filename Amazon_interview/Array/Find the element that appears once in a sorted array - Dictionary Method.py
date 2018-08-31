def find(arr):
    temp = {}
    for item in arr:
        if item in temp:
            temp[item] += 1
        else:
            temp[item] = 1

    for key,value in temp.items():
        if value == 1:
            print(key)



def main():
    arr = [1,1,3,3,4,5,5,7,7,8,8]
    find(arr)

main()
