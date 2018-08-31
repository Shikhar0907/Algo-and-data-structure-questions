def countWord(string,n):
    dic = {}
    for item in string:
        if item in dic:
            dic[item] += 1
        else:
            dic[item] = 1
    print(dic)



def main():
    s = [ "hate", "love", "peace", "love",
      "peace", "hate", "love", "peace",
                "love", "peace" ]
    n = len(s)
    countWord(s,n)


main()
