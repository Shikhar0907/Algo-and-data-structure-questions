def check(string,buff):
    low = 0
    mid = 1
    high = len(string)-1
    buff[0] = 0
    count = 0
    while mid < high:
        if string[mid] == string[low]:
            count +=1
            buff[mid] = count
            mid += 1
            low += 1
        else:
            buff[mid] = count
            mid += 1
            

def main():
    string = "abcabc"
    n = len(string)
    buff = [0] * len(string)
    check(string,buff)
    count = buff[-1]
    if n%(n-count) == 0:
        print("Yes")
    else:
        print("No")

main()
