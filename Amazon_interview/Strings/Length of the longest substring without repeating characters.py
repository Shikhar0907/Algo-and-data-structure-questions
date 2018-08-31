def Unique(string):
    visited = [-1] * 256
    cur_len = 1
    max_len = 1
    prev_index = 0
    
    visited[ord(string[0])] = 0
    #print(visited)

    for i in range(1,len(string)):
        prev_index = visited[ord(string[i])]

        if prev_index == -1 or (i - cur_len > prev_index):
            cur_len +=1
        else:
            if cur_len > max_len:
                max_len = cur_len
            cur_len = i - prev_index

        visited[ord(string[i])] = i


    if cur_len > max_len:
        max_len = cur_len

    return(max_len)



def main():
    string = "ABDEFGABEF"
    print(Unique(string))


main()
