# Problem 1476A - K-Divisible Sum

def main():
    T = int(input())
    for c in range(T):
        inp = input().rstrip().split(" ")
        n, k = int(inp[0]), int(inp[1])
        if n <= k:
            if k % n == 0:
                print(int(k/n))
            else:
                print(int(k/n)+1)
        else:
            if n % k == 0:
                print(1)
            else:
                print(2)
            

main()
