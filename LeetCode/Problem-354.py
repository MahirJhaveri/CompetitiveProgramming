# 354 - Russian Doll Envelopes

import math

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        N = len(envelopes)
        envelopes.sort(key=lambda tup: (tup[0], -1*tup[1]))
        arr = [envelopes[i][1] for i in range(N)]
        d = [math.inf for i in range(N+1)]
        d[0] = -1*math.inf
        
        ans = 0
        for i in range(N):
            j = bsearch(d, arr[i])
            d[j+1] = min(d[j+1], arr[i])
            ans = max(ans, j+1)
        return ans
            
        
def bsearch(d, val):
    start = 0
    end = len(d)
    mid = int((start+end)/2)
    while start < mid:
        if d[mid] >= val:
            end = mid
        else:
            start = mid
        mid = int((start+end)/2)
    return start
