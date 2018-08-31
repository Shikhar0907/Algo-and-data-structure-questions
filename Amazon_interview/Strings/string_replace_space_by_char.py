def replace_space(string):
    st = ""
    for item in string:
        if item == " ":
            st = st + "%20"
        else:
            st = st + item
    print(st)



def main():
    string = str(input("Please enter the string: "))
    replace_space(string)


main()
    
