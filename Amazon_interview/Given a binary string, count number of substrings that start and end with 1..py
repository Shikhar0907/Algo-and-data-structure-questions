def binary_strings(string):
    count = 0
    for i in range(len(string)):
        if string[i] == '1':
            count += 1
    count = count *(count-1)/2
    print(int(count))
    



def main():
    string = "00100101"
    binary_strings(string)

main()
