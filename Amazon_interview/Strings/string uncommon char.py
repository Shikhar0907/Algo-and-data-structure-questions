def uncommon(str1,str2):
    temp = set()
    for item in str2:
        if item in str1:
            pass
        else:
            temp.add(item)

    for item in str1:
        if item in str2:
            pass
        else:
            temp.add(item)

    print(temp)
    




def main():
    str1 = "characters"
    str2 = "alphabets"
    uncommon(str1,str2)

main()
