# 1411 - Number of ways to paint N*3 grid

class Solution(object):
    def numOfWays(self, n):
        MOD = 1000000007
        ans1 = ans2 = 6
        i = 1
        while i < n:
            temp = ans1
            ans1 = (3*ans1 + 2*ans2) % MOD
            ans2 = (2*temp + 2*ans2) % MOD
            i += 1
        return (ans1 + ans2) % MOD
