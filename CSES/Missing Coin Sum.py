# Missing Coin Sum
 
def main():
    n = int(input())
    x = input().rstrip().split(" ")
    s = 0
    for i in range(len(x)):
        x[i] = int(x[i])
    x.sort()
    for i in range(len(x)):
        if x[i] > s+1:
            print(s+1)
            return
        s += x[i]
    print(s+1)
 
main()
