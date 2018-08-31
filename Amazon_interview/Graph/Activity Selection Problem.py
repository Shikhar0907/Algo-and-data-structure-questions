def print_activities(start,finish):
    n = len(finish)
    i = 0
    print(i)
    for j in range(n):
        if start[j] >= finish[i]:
            print(j)
            i = j


def main():
    start = [1,3,0,5,8,5]
    finish = [2,4,6,7,9,9]
    print_activities(start,finish)


main()
