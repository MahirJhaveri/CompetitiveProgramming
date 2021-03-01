# Problem 1492D - Genius's Gambit

def main():
    inp = input().rstrip().split(" ")
    a,b,k = int(inp[0]), int(inp[1]), int(inp[2])
    x = []
    y = []
    if b == 1 or a == 0:
        if k == 0:
            print('Yes')
            for _ in range(b):
                x.append("1")
                y.append("1")
            for _ in range(a):
                x.append("0")
                y.append("0")
            print("".join(x))
            print("".join(y))
        else:
            print('No')
    elif k > a+b-2:
        print("No")
    else:
        print("Yes")
        if k <= a:
            y.append("1")
            for _ in range(k):
                x.append("0")
                y.append("0")
            x.append("1")
            for _ in range(k, a):
                x.append("0")
                y.append("0")
            for _ in range(b-1):
                x.append("1")
                y.append("1")
            x.reverse()
            y.reverse()
        else:
            for _ in range(b):
                x.append("1")
                y.append("1")
            for _ in range(a):
                x.append("0")
                y.append("0")
            y[-1] = "1"
            y[a+b-2-k+1] = "0"
        print("".join(x))
        print("".join(y))

main()
