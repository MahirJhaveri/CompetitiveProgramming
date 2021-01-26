# Problem 1475B - New Year's New Number

import math

def main():
    T = int(input())
    for c in range(T):
        n = int(input())
        remainder = n % 2020
        quotient = 0
        while (quotient+1)*2020 <= n:
            quotient += 1
        if quotient >= remainder:
            print("YES")
        else:
            print("NO")

main()
