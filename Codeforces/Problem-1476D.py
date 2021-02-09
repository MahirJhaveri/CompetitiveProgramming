# Problem 1476D - Journey

l_dp0 = [0 for x in range(300001)]
l_dp1 = [0 for x in range(300001)]
r_dp0 = [0 for x in range(300001)]
r_dp1 = [0 for x in range(300001)]

def reset(n):
    for i in range(n+1):
        l_dp0[i] = 0
        l_dp1[i] = 0
        r_dp0[i] = 0
        r_dp1[i] = 0

def solve():
    n = int(input())
    arr = input().rstrip()
    
    reset(n)
    
    # compute left
    l_dp0[0] = 1
    l_dp1[0] = 1
    for i in range(1,n+1):
        l_dp0[i] = l_dp1[i-1] + 1 if arr[i-1] == 'L' else 1
        l_dp1[i] = 1 if arr[i-1] == 'L' else l_dp0[i-1] + 1
    
    # compute right
    r_dp0[n] = 1
    r_dp1[n] = 1
    for i in reversed(range(n)):
        r_dp0[i] = r_dp1[i+1] + 1 if arr[i] == 'R' else 1
        r_dp1[i] = 1 if arr[i] == 'R' else r_dp0[i+1] + 1
    
    ans = [str(l_dp0[i] + r_dp0[i] - 1) for i in range(n+1)]
    print(" ".join(ans))

def main():
    T = int(input())
    for c in range(T):
        solve()
main()
