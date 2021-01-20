# Problem 1474A - Puzzle From The Future
def main():
    T = int(input())
    for c in range(T):
        n = int(input())
        b = input().rstrip()
        a = ""
        prev = 0
        for i in range(n):
            if int(b[i])+1 != prev:
                a += "1"
                prev = int(b[i])+1
            else:
                a += "0"
                prev = int(b[i])
        print(a)

main()
