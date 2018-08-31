def duplicate(string):
    temp = {}
    for item in string:
        if item in temp:
            temp[item] += 1
        else:
            temp[item] = 1
    for key, value in temp.items():
        if value > 1:
            print(key, value)
        



def main():
    string = str(input("Please enter the string: "))
    duplicate(string)

main()
