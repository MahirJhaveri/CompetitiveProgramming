# Problem 1463B - Find The Array

def gen_beautiful_arr(arr, parity):
    res = []
    for c in range(len(arr)):
        if c % 2 == parity:
            res.append(arr[c])
        else:
            res.append("1")
    return res

def main():
    T = int(input())
    for c in range(T):
        n = int(input())
        arr = input().rstrip().split(" ")
        s_even = s_odd = 0
        for c in range(n):
            if c % 2 == 0:
                s_odd += (int(arr[c]) - 1)
            else:
                s_even += (int(arr[c]) - 1)
        print(" ".join(gen_beautiful_arr(arr, 1 if s_odd < s_even else 0)))
main()
