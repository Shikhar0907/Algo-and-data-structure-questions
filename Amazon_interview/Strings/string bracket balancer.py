def balance_paranthesis(string):
    opening = ("{","(","[")
    closing = ("}",")","]")
    mapping = {opening[0]:closing[0],
               opening[1]:closing[1],
               opening[2]:closing[2]}

    if string[0] in closing:
        return(False)
    if string[-1] in opening:
        return(False)

    queue = []
    for letter in string:
        if letter in opening:
            queue.append(mapping[letter])
        elif letter in closing:
            if not queue:
                return(False)
            if queue[-1] == letter:
                queue.pop()
            else:
                return(False)
    return(True)




def main():
    string = str(input("Please enter the string: "))
    print(balance_paranthesis(string))


main()
