# 556. Next Greater Element III

def sort(arr, pos):
    f = [0 for i in range(0,11)]
    for d in arr[0:pos]:
        f[d] += 1
    d = 9
    p = 0
    while p < pos:
        while d >= 0 and f[d] > 0:
            arr[p] = d
            f[d] -= 1
            p += 1
        d -= 1
    return

class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return -1
        
        arr = []
        m = n
        while m > 0:
            arr.append(m % 10)
            m = m / 10
        
        i = 0
        stack = []
        while i < len(arr):
            pos, val = None, None
            while len(stack) > 0 and arr[i] < stack[-1][1]:
                pos, val = stack.pop()
            if pos != None:
                arr[pos] = arr[i]
                arr[i] = val
                break
            stack.append((i, arr[i]))
            i += 1
            
        # sort the positions 0:i of arr in ascending order
        sort(arr, i)
        
        # n is largest of its kind
        if i == len(arr):
            return -1
        
        num = 0
        i = 0
        while i < len(arr):
            num += arr[i] * (10 ** i)
            i += 1
        
        if num > 2147483647:
            return -1
        return num
