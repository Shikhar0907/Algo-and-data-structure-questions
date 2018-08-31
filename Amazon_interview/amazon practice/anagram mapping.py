def anagram(arr1,arr2):
    temp = {}
    for i in range(len(arr2)):
        temp[arr2[i]] = i
    print(temp)

    for i in range(len(arr1)):
        print(str(temp[arr1[i]]),end= " ")

def main():
    arr1 = [12,28,46,32,50]
    arr2 = [50,12,32,46,28]
    anagram(arr1,arr2)

main()
