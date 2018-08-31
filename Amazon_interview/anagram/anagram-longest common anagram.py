def anagram(string1,string2):
    temp = set()
    for item in string1:
        if item in string2:
            if item not in temp:
                temp.add(item)

    print(temp)
    




def main():
    string1 = str(input("Please enter the string: "))
    string2 = str(input("Please enter the string: "))
    anagram(string1,string2)

main()
