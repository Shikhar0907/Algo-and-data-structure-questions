def NumOfTimes(string1,string2):
    freq = {}
    for item in string1:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    count = 12335
    for item in string2:
        count = min(count,freq[item])
    print(count)




def main():
    string1 = str(input("Please enter the string1: "))
    string2 = str(input("Please enter the string2: "))
    NumOfTimes(string1,string2)


main()
