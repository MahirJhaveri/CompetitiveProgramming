#Problem 1476B - Inflation

import math

def main():
    T = int(input())
    for c in range(T):
        inp = input().rstrip().split(" ")
        n, k = int(inp[0]), int(inp[1])
        arr = input().rstrip().split(" ")
        p0 = int(arr[0])
        cum_sum = 0
        for i in range(1,n):
            pi = int(arr[i])
            if pi*100/(cum_sum+p0) > k:
                p0 = int(math.ceil(pi*100/k) - cum_sum)
            cum_sum += pi
        print(int(p0 - int(arr[0])))

main()
