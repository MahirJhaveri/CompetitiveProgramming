# Josephus I

def solve(arr, res, start=0):
    if len(arr) == 1:
        res.append(str(arr[-1]))
    else:
        new_arr = []
        for i in range(len(arr)):
            if (i + start + 1) % 2 == 0:
                res.append(str(arr[i]))
            else:
                new_arr.append(arr[i])
        solve(new_arr, res, start=(len(arr)+start)%2)
                

def main():
    n = int(input())
    arr = []
    for i in range(1,n+1):
        arr.append(i)
    res = []
    solve(arr, res)
    print(" ".join(res))
    

main()
