def encode(string,k):
    new_string = ""
    for i in range(len(string)):
        val = ord(string[i])

        new_string += chr(val+k)

    print(new_string)


def main():
    string = str(input("Please enter the string: "))
    k = 2
    encode(string,k)


main()
