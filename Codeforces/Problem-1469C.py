# Problem 1469C - Building A Fence

def solve():
    inp = input().rstrip().split(" ")
    n, k = int(inp[0]), int(inp[1])
    arr = input().rstrip().split(" ")
    for i in range(n):
        arr[i] = int(arr[i])
    r = [arr[0], arr[0]]
    for i in range(1,n):
        new_r = [max(r[0]-(k-1), arr[i]), min(r[1]+(k-1), arr[i]+(k-1))]
        if new_r[0] > new_r[1]:
            print("NO")
            return
        r = new_r
    if not (r[0] <= arr[-1] and arr[-1] <= r[1]):
        print("NO")
        return
    print("YES")

def main():
    T = int(input())
    for c in range(T):
        solve()

main()
