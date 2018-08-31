def freq(arr,num):
    dic = {}
    for item in arr:
        if item not in dic:
            dic[item] = 1
        else:
            dic[item] += 1
    print(dic[num])




def main():
    arr = list(map(int,input("Please enter the elements: ").split()))
    num = int(input("Please enter the number: "))
    freq(arr,num)


main()
