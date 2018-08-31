def stack(arr):
    st = []
    for i in range(len(arr)):
        while len(st) != 0 and st[-1] >= arr[i]:
            st.pop()
            
        if len(st) == 0:
            print("_,",end="")
        else:
            print(" %d,"%st[-1],end="")
        
        st.append(arr[i])


def main():
    arr = [1,3,0,2,5]
    stack(arr)

main()
