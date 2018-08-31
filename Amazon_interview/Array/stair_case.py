def stair_case(num):
    if num <=1:
        return(num)
    return(stair_case(num-1) + stair_case(num-2))


def main():
    num = 4
    print(stair_case(num+1))


main()
