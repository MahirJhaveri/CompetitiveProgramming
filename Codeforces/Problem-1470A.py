# Problem 1470A - Codeforces - Strange Birthday Party
def main():
    T = int(input())
    for c in range(T):
        inp = input().rstrip().split(" ")
        n, m = int(inp[0]), int(inp[1])
        k_arr = input().rstrip().split(" ")
        for i in range(n):
            k_arr[i] = int(k_arr[i])-1
        c_arr = input().rstrip().split(" ")
        for i in range(m):
            c_arr[i] = int(c_arr[i])
        
        k_arr.sort()
        
        ans = 0
        i = 0
        while len(k_arr) > 0:
            if i < m and c_arr[i] < c_arr[k_arr[-1]]:
                ans += c_arr[i]
                i += 1
            else:
                ans += c_arr[k_arr[-1]]
            k_arr.pop()
        print(ans)
                

main()
