# Problem 1476C - Longest Simple Cycle

def main():
    T = int(input())
    for c in range(T):
        n = int(input())
        c = input().rstrip().split(" ")
        a = input().rstrip().split(" ")
        b = input().rstrip().split(" ")
        oldl = maxl = 0
        for i in range(1, n):
            l = 0
            ai,bi,ci = int(a[i]),int(b[i]),int(c[i])
            if ai != bi:
                l = ci + 1 + max(abs(ai-bi), oldl - abs(ai-bi))
            else:
                l = ci + 1
            maxl = max(maxl, l)
            oldl = l
        print(maxl)
main()
