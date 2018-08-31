def set_bits(num):
    count = 0
    while num> 0:
        count += num & 1
        print(count)
        num >>= 1
    return(count)

def find_bits(num):
    bit_count = 0

    for i in range(1,num+1):
        bit_count += set_bits(i)

    return(bit_count)


def main():
    num = 3
    #count = 0
    print(find_bits(num))


main()
