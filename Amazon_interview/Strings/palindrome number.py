def palindrome_number(num):
    if num == 0:
        return(num)
    temp = num
    add = 0
    while num != 0:
        digit = num%10
        add = (add*10) + digit
        num = num//10
    if add == temp:
         print("True")
    else:
        print("False")




def main():
    num = int(input("Please enter the number: "))
    palindrome_number(num)


main()
