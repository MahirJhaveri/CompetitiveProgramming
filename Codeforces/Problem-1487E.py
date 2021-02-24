# Problem 1487E - Cheap Dinner

from math import inf

def main():
    inp = input().rstrip().split(" ")
    n1, n2, n3, n4 = int(inp[0]), int(inp[1]), int(inp[2]), int(inp[3])
    a = input().rstrip().split(" ")
    b = input().rstrip().split(" ")
    c = input().rstrip().split(" ")
    d = input().rstrip().split(" ")
    m1 = int(input())
    hm1 = {}
    for x in range(m1):
        inp = input().rstrip().split(" ")
        hm1[(int(inp[0]), int(inp[1]))] = True
    m2 = int(input())
    hm2 = {}
    for x in range(m2):
        inp = input().rstrip().split(" ")
        hm2[(int(inp[0]), int(inp[1]))] = True
    m3 = int(input())
    hm3 = {}
    for x in range(m3):
        inp = input().rstrip().split(" ")
        hm3[(int(inp[0]), int(inp[1]))] = True
    
    a = [(i+1, int(a[i])) for i in range(n1)]
    b = [(i+1, int(b[i])) for i in range(n2)]
    c = [(i+1, int(c[i])) for i in range(n3)]
    d = [(i+1, int(d[i])) for i in range(n4)]
    
    a.sort(key=lambda tup: tup[1])
    arr = [a,b,c,d]
    hm = [hm1,hm2,hm3]
    for i in range(1,4):
        for j in range(len(arr[i])):
            k=0
            while k < len(arr[i-1]):
                if (arr[i-1][k][0], arr[i][j][0]) not in hm[i-1]:
                    arr[i][j] = (arr[i][j][0], arr[i][j][1]+arr[i-1][k][1])
                    break
                k += 1
            if k == len(arr[i-1]):
                arr[i][j] = (arr[i][j][0], inf)
        arr[i].sort(key=lambda tup: tup[1])
    ans = arr[-1][0][1]
    if ans == inf:
        print(-1)
    else:
        print(ans)
    

main()
