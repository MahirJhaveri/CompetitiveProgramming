# Problem 1475E - Advertising Agency

table = {}

def nCr(n, r):
    if (n,r) in table:
        return table[(n,r)]
    elif r == 0:
        return 1
    elif r == 1:
        return n
    elif n == r:
        return 1
    else:
        table[(n,r)] = (nCr(n-1,r) + nCr(n-1,r-1)) % 1000000007
        return table[(n,r)]

def main():
    T = int(input())
    for c in range(T):
        inp = input().rstrip().split(" ")
        n, k = int(inp[0]), int(inp[1])
        arr = input().rstrip().split(" ")
        
        hmap = {}
        for i in range(n):
            if int(arr[i]) not in hmap:
                hmap[int(arr[i])] = 0
            hmap[int(arr[i])] += 1
        arr = list(hmap.keys())
        arr.sort(reverse=True)
        m=0
        i=0
        while not (m+hmap[arr[i]] >= k):
            m += hmap[arr[i]]
            i += 1
        print(nCr(hmap[arr[i]], k-m))

main()
