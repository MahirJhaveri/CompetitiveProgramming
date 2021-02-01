# Problem 1475G - Strange Beauty

def solve():
    n = int(input())
    arr = input().rstrip().split(" ")
    cnt = {}
    for i in range(n):
        arr[i] = int(arr[i])
        if arr[i] not in cnt:
            cnt[arr[i]] = 0
        cnt[arr[i]] += 1
    arr = list(cnt.keys())
    arr.sort()
    table = {}
    ans  = 0
    for i in range(1,arr[-1]+1):
        if i not in table:
            table[i] = 0
        table[i] += cnt[i] if i in cnt else 0
        ans = max(ans, table[i])
        j = 2*i
        while j < arr[-1]+1:
            if j not in table:
                table[j] = 0
            table[j] = max(table[i], table[j])
            j += i
    print(n - ans)
        

def main():
    T = int(input())
    for c in range(T):
        solve()

main()
