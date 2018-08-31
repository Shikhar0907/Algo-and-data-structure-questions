def anagram(string):
    max_num = 0
    string = string.split()
    for i in range(len(string)):
        string[i] = ''.join(sorted(string[i]))
    temp = {}
    for item in string:
        if item not in temp:
            temp[item] = 1
        else:
            temp[item] += 1

    print(max(temp.items(), key = lambda x: x[1]))
    





def main():
    string = "ant magenta magnate tan gnamate"
    anagram(string)


main()
