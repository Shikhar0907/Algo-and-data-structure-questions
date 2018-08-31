def anagram(string1,string2):
    count = 0
    temp = set()
    for item in string1:
        if item in string2:
            if item not in temp:
                temp.add(item)
            else:
                count += 1
        else:
            count += 1
    print(count)



def main():
    string1 = str(input("Please enter the elements: "))
    string2 = str(input("Please enter the elements: "))
    anagram(string1,string2)

main()
