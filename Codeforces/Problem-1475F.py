# Problem 1475F - Unusual Matrix

def solve():
    n = int(input())
    a1 = []
    a2 = []
    for i in range(n):
        arr = input().rstrip()
        a1.append([int(arr[x]) for x in range(n)])
        a2.append([int(arr[x]) for x in range(n)])
    input()
    b = []
    for i in range(n):
        arr = input().rstrip()
        b.append([int(arr[x]) for x in range(n)])
    
    for j in range(n):
        a2[0][j] == 1-a2[0][j]
        if a1[0][j] == b[0][j]:
            for i in range(n):
                a2[i][j] = 1-a2[i][j]
        else:
            for i in range(n):
                a1[i][j] = 1-a1[i][j]
    r1 = r2 = True
    
    for i in range(1,n):
        s1 = s2 = 0
        for j in range(n):
            s1 += abs(a1[i][j] - b[i][j])
            s2 += abs(a1[i][j] + b[i][j] - 1)
        if s1 != 0 and s2 != 0:
            r1 = False
    
    for i in range(1,n):
        s1 = s2 = 0
        for j in range(n):
            s1 += abs(a2[i][j] - b[i][j])
            s2 += abs(a2[i][j] + b[i][j] - 1)
        if s1 != 0 and s2 != 0:
            r2 = False
    
    if r1 or r2:
        print("YES")
    else:
        print("NO")

def main():
    T = int(input())
    for c in range(T):
        solve()

main()
