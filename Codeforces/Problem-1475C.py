# Problem 1475C - Ball in Berland

def solve():
    inp = input().rstrip().split(" ")
    a,b,k = int(inp[0]),int(inp[1]),int(inp[2])
    arr1 = input().rstrip().split(" ")
    arr2 = input().rstrip().split(" ")
    bmap = {}
    gmap = {}
    ans  = 0
    for i in range(k):
        arr1[i] = int(arr1[i])
        arr2[i] = int(arr2[i])
        if arr1[i] not in bmap:
            bmap[arr1[i]] = 0
        if arr2[i] not in gmap:
            gmap[arr2[i]] = 0
        ans += i - (bmap[arr1[i]] + gmap[arr2[i]])
        bmap[arr1[i]] += 1
        gmap[arr2[i]] += 1
    print(ans)
        

def main():
    T = int(input())
    for c in range(T):
        solve()

main()
