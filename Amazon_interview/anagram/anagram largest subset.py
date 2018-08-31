def anagram(string):
    string = string.split()
    for i in range(len(string)):
        string[i] = ''.join(sorted(string[i]))
    temp = set(string)
    current_count = 0
    max_count = 0
    for item in list(temp):
        for j in range(len(string)):
            if item == string[j]:
                current_count += 1
        if current_count > max_count:
            max_count = current_count
        current_count =0

    print(max_count)
    
    



def main():
    string = str(input("Please enter the string: "))
    anagram(string)



main()
