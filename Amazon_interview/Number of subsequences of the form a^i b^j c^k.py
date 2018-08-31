def subsequence(string):
    a_count = 0
    b_count = 0
    c_count = 0
    for i in range(len(string)):
        if string[i] == 'a':
            a_count = 1 + (2 * a_count)
            print(a_count)
        elif string[i] == 'b':
            b_count = a_count + 2*b_count
            print(b_count)
        elif string[i] == 'c':
            c_count = b_count + 2* c_count
            print(c_count)

    return(c_count)



def main():
    string = "abbc"
    subsequence(string)


main()
