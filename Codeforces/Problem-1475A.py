# Problem 1475A - Odd Divisor

def main():
    T = int(input())
    for c in range(T):
        n = int(input())
        while 2*(n >> 1) == n:
            n = n >> 1
        if n > 1:
            print("YES")
        else:
            print("NO")

main()
