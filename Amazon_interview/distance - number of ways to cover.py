def distance(num):
    if num < 0:
        return(0)
    if num == 0:
        return(1)
    return(distance(num-1) + distance(num-2) + distance(num-3))



def main():
    num = 4
    print(distance(num))

main()
