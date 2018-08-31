def Binary_search_tree(arr):
    s = []
    root = -233425434
    for val in arr:
        if val < root:
            return(False)

        if len(s)> 0 and s[-1] < val:
            root = s.pop()

        s.append(val)
    return(True)




def main():
    arr = [40,30,35,80,100]
    print(Binary_search_tree(arr))

main()
        
