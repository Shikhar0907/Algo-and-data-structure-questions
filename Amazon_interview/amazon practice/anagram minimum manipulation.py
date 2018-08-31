def anagram(string1,string2):
    count = 0
    temp = set()
    for item in string2:
        if item in string1:
            if item not in temp:
                count += 1
    print(count)
                
        
    



def main():
    string1 = "ddcf"
    string2 = "cedk"
    anagram(string1,string2)


main()
