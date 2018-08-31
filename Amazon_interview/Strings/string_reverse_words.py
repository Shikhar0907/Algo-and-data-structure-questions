def reverse_words(string):
    st = string.split()
    sentance = []
    for i in range(len(st)-1,-1,-1):
        sentance.append(st[i])
    print(' '.join(sentance))




def main():
    string = str(input("Please enter the string: "))
    reverse_words(string)


main()
