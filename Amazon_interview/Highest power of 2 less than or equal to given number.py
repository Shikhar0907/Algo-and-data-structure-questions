'''
Application Problem:
Some people are standing in a queue.
A selection process follows a rule where people standing on even positions are selected. Of the selected people a queue is formed and again out of these only people on even position are selected. This continues until we are left with one person.
Find out the position of that person in the original queue.
'''

def highest_power_two(num):
    for i in range(num,0,-1):
        if i & (i-1) == 0:
            return(i)
        



def main():
    num = 17
    print(highest_power_two(num))


main()
