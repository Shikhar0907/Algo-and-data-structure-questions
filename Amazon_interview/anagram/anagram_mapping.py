def anagram_mapping(arr1,arr2):
    temp = {}
    new_array = []
    for i in range(len(arr2)):
        temp[arr2[i]] = i
    for i in range(len(arr1)):
        new_array.append(temp[arr1[i]])

    print(new_array)

def main():
    arr1 = list(map(int,input("Please enter the elements: ").split()))
    arr2 = list(map(int,input("Please enter the elements: ").split()))
    anagram_mapping(arr1,arr2)



main()
