# CodeJam 2021 Qualification Round - Reversort Engineering

def reverse(arr, i, j):
    temp = []
    for c in range(i, j+1):
        temp.append(arr[c])
    temp.reverse()
    for t in range(j+1-i):
        arr[i+t] = temp[t]

def main():
    T = int(input())
    for c in range(1, T+1):
        inp = input().rstrip().split(" ")
        N, C = int(inp[0]), int(inp[1])
        if C < N-1 or C >= N*(N+1)/2:
            print("Case #%d: IMPOSSIBLE" % c)
        else:
            final = [None for i in range(N)]
            C -= N-1
            curr = 1
            arr = [i for i in range(N)]
            i = 0
            while i < N-1 and C > 0:
                j = i
                while j < N-1 and C > 0:
                    j += 1
                    C -= 1
                final[arr[j]] = str(curr)
                curr += 1
                reverse(arr, i, j)
                i += 1
            while i < N:
                final[arr[i]] = str(curr)
                curr += 1
                i += 1
            ans = " ".join(final)
            print("Case #%d: %s" % (c, ans))

main()
