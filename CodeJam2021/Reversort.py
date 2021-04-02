# CodeJam 2021 Qualification Round - Reversort

import math

def find_min(arr, i):
    min_val = math.inf
    min_pos = None
    for j in range(i,len(arr)):
        if arr[j] < min_val:
            min_val = arr[j]
            min_pos = j
    return min_pos

def reverse(arr, i, j):
    temp = []
    for x in range(i,j+1):
        temp.append(arr[x])
    temp.reverse()
    for t in range(len(temp)):
        arr[i+t] = temp[t]

def reverse_sort_cost(arr):
    cost = 0
    for i in range(len(arr)-1):
        j = find_min(arr, i)
        reverse(arr, i, j)
        cost += (j-i+1)
    return cost

def main():
    T = int(input())
    for c in range(1,T+1):
        n = int(input())
        inp = input().rstrip().split(" ")
        arr = []
        for val in inp:
            arr.append(int(val))
        ans = reverse_sort_cost(arr)
        print("Case #%d: %d" % (c, ans))

main()
