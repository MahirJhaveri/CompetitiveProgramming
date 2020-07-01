# Problem 978 - Longest Turbulent Subarray

class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        if len(A) == 1:
            return 1
       
        i = 1
        curr = 1 if A[1] - A[0] != 0 else 0
        ans = curr
        while i < len(A)-1:
            if (A[i] - A[i-1])*(A[i+1]-A[i]) < 0:
                curr += 1
                if curr > ans:
                    ans = curr
            else:
                curr = 1
            i += 1
        return ans+1
