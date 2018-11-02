isValid = False
def arithmetic_boggle(magic_number, numbers):
    global isValid
    # Fill in the code
    #print(numbers)
    ans = findPossibility(numbers,0,0,magic_number)
    return(isValid)
    

def findPossibility(arr,i,s,num):
    global isValid

    if i == len(arr):
        
        if s== num:
            isValid = True        
            return(isValid)

    if(i+1<=len(arr) and isValid == False):
        findPossibility(arr, i+1,s + arr[i], num)  
        findPossibility(arr, i+1,s - arr[i], num)
    return(isValid)

print(arithmetic_boggle(4,[5]))
    


