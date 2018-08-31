def count_vowels(string):
    count_vowels = 0
    count_consonants = 0
    vowels = ['a','e','i','o','u']
    for item in string:
        if item in vowels:
            count_vowels +=1
        else:
            count_consonants += 1
            
    return(count_vowels,count_consonants)







def main():
    string = str(input("Please enter the string: "))
    print(count_vowels(string))


main()
