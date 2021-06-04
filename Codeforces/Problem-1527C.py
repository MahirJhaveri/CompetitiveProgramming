# Problem 1527C - Sequence Pair Weight
def main():
    T = int(input())
    for c in range(1,T+1):
        n = int(input())
        arr = input().rstrip().split(" ")
        for i in range(n):
            arr[i] = int(arr[i])
        d = {}
        ans = 0
        for i in range(n):
            l = i+1
            r = n-i
            if arr[i] not in d:
                d[arr[i]] = l
            else:
                ans += d[arr[i]]*r
                d[arr[i]] += l
        print(ans)

main()
