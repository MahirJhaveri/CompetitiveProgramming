# Problem 1360E - Polygon

T = int(input())
for t in range(T):
    n = int(input())
    M = []
    
    row = 0
    while row < n:
        data = input().rstrip().split()
        i=0
        while i<n:
            data[i] = int(data[i])
            i+=1
        M.append(data)
        row+=1
    
    exit=False
    
    row=0
    while row<n:
        col=0
        while col<n:
            if(M[row][col] == 1):
                if col+1!=n and row+1!=n:
                    if M[row+1][col]!=1 and M[row][col+1]!=1:
                        print("NO")
                        exit=True
                M[row][col]=0
            col+=1
        if exit:
            break
        row+=1
    
    if not exit:
        print("YES")
