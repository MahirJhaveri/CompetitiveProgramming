# Problem-907.py : Sum of subarray minimums

class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ans  = 0
        arr = []
        i = 0
        while i < len(A):
            while len(arr) > 0 and arr[-1][0] >= A[i]:
                top = arr.pop()
                if len(arr) > 0:
                    ans = (ans + (i - top[1])*top[0]*(top[1]-arr[-1][1])) % 1000000007
                else:
                    ans = (ans + (i - top[1])*top[0]*(top[1]+1)) % 1000000007
            arr.append((A[i], i))
            i += 1
        
        print(arr)
        
        i = len(A)
        while len(arr)>0:
            top = arr.pop()
            if len(arr) > 0:
                ans = (ans + (i - top[1])*top[0]*(top[1]-arr[-1][1])) % 1000000007
            else:
                ans = (ans + (i - top[1])*top[0]*(top[1]+1)) % 1000000007
        
        return ans
