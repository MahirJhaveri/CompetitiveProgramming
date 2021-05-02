# Problem 5749 - Minimum Adjacent Swaps to Reach the Kth Smallest Number

import copy


def qsort(num, i):
    arr = []
    j=i
    while j < len(num):
        arr.append(int(num[j]))
        j += 1
    arr.sort()
    j=0
    while j < len(num)-i:
        num[j+i] = str(arr[j])
        j += 1
    return

def getNextPerm(num):
    new_num = list(num)
    d = [-1 for j in range(10)]
    n = 0
    for i in reversed(range(len(num))):
        if int(new_num[i]) < n:
            for k in range(int(new_num[i])+1, 10):
                if d[k] != -1:
                    new_num[d[k]] = new_num[i]
                    new_num[i] = str(k)
                    qsort(new_num, i+1)
                    break
            break
        else:
            n = int(new_num[i])
            d[int(new_num[i])] = i
    return "".join(new_num)

class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        new_num = num
        for i in range(k):
            new_num = getNextPerm(new_num)
        
        num = list(num)
        new_num = list(new_num)
        
        i=0
        ans = 0
        while i < len(num):
            if num[i] != new_num[i]:
                j=i
                n = new_num[i]
                while True:
                    if num[j] == new_num[i]:
                        num[j] = n
                        break
                    else:
                        temp = num[j]
                        num[j] = n
                        n = temp
                        j += 1
                ans += (j-i)
            i += 1
        return ans
        
        
