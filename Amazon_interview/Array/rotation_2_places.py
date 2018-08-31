def left_rotate():
    return(str2[2:] + str2[0:2])
    
    


def right_rotate(str2):
    return(str2[len(str2)-2:len(str2)] + str2[:len(str2)-2])



def string_rotation(str1,str2):
    if len(str1) != len(str2):
        return(False)
    anti_clock = right_rotate(str2)
    if anti_clock == str1:
        return(True)
    clock = left_rotate(str2)
    if clock == str1:
        return(True)
    return(False)
    

def main():
    str1 = str(input("Please enter the string1: "))
    str2 = str(input("Please enter the string2: "))
    if (string_rotation(str1,str2)) == True:
        print("Yes")
    else:
        print("No")

main()
