def reverse_string(string):
    if len(string) == 0:
        return(string)
    return(string[-1:] + reverse_string(string[:-1]))



def main():
    string = str(input("Please enter the string: "))
    print(reverse_string(string))

main()
