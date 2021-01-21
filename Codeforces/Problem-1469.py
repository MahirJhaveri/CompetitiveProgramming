# Problem 1469B - Red and Blue

def solve():
    n = int(input())
    r = input().rstrip().split(" ")
    m = int(input())
    b = input().rstrip().split(" ")
    
    rmax = bmax = 0
    csum = 0
    for i in range(n):
        csum += int(r[i])
        rmax = max(rmax, csum)
    csum = 0
    for i in range(m):
        csum += int(b[i])
        bmax = max(bmax, csum)
    print(rmax + bmax)

def main():
    T = int(input())
    for c in range(T):
        solve()

main()
