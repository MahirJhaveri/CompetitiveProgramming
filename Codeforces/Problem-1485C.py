# Problem 1485C - Floor and Mod

import math

def main():
    T = int(input())
    for c in range(T):
        inp = input().rstrip().split(" ")
        x, y = int(inp[0]), int(inp[1])
        ans  = 0
        k = 1
        while k*k < x and k < y:
            temp = min(y, math.floor(x/k)-1) - k
            if temp > 0:
                ans += temp
            k += 1
        print(ans)
    
main()
