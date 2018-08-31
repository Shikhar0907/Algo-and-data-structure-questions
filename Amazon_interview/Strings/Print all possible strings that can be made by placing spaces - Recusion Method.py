def toString(arr):
    s = ""
    for x in arr:
        if x == '\0':
            break
        s += x
    return(s)




def placing_space(string,buff,i,j,n):
    if i == n:
        buff[j] = '\0'
        print(toString(buff))
        return
    buff[j] = string[i]
    placing_space(string,buff,i+1,j+1,n)

    buff[j] = ' '
    buff[j+1] = string[i]

    placing_space(string,buff,i+1,j+2,n)




def main():
    string = "ABCD"
    buff = [0]* 2*len(string)
    buff[0] = string[0]
    placing_space(string,buff,1,1,len(string))


main()

    
