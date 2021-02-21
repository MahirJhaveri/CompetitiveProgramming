# Problem 1490F - Equalize the Array

def main():
    T = int(input())
    for c in range(T):
        n = int(input())
        h = {}
        inp = input().rstrip().split(" ")
        for x in inp:
            if int(x) not in h:
                h[int(x)] = 1
            else:
                h[int(x)] += 1
        arr = []
        for k in h.keys():
            arr.append(h[k])
        arr.sort(reverse=True)
        ans = 0
        for i in range(len(h)):
            ans = max(ans, arr[i]*(i+1))
        print(n - ans)

main()
