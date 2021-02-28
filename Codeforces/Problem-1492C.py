# Problem 1492C - Maximum Width

def main():
    inp = input().rstrip().split(" ")
    n, m = int(inp[0]), int(inp[1])
    s = input().rstrip()
    t = input().rstrip()
    
    fwd_arr=[0 for i in range(m)]
    bwd_arr=[0 for i in range(m)]
    fpos = 0
    bpos = n-1
    for i in range(m):
        while s[fpos] != t[i]:
            fpos+=1
        fwd_arr[i] = fpos
        fpos += 1
        while s[bpos] != t[m-1-i]:
            bpos-=1
        bwd_arr[m-1-i]=bpos
        bpos -= 1
    ans=0
    for i in range(m-1):
        ans = max(ans, bwd_arr[i+1]-fwd_arr[i])
    print(ans)

main()
