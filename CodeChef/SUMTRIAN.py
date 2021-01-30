# SUMTRIAN - Sums in a triangle

def main():
    T = int(input())
    for c in range(T):
        n = int(input())
        ans = 0
        old_arr = [int(input())]
        for i in range(n-1):
            arr = input().rstrip().split(" ")
            for x in range(len(arr)):
                arr[x] = int(arr[x])
            arr[0] = old_arr[0] + arr[0]
            for x in range(1,len(old_arr)):
                arr[x] = max(old_arr[x], old_arr[x-1]) + arr[x]
            arr[-1] = old_arr[-1] + arr[-1]
            old_arr = arr
        print(max(old_arr))

main()
