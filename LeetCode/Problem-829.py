# Problem 829 - Consecutive Numbers Sum

class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        d = 2
        count = 1
        while d*(d-1) < 2*N:
            diff = N - d*(d-1)/2
            if diff >= d and diff % d == 0:
                count += 1
            d += 1
        return count
        
