# Leetcode 940 - Distinct Subsequences II
# Use DP to solve the problem

class Solution(object):
    def distinctSubseqII(self, S):
        n = len(S)
        # holds the number of unique sequences starting with some char
        X = {}
        # number of unique strings between [i:end]. So, Y[0]-1 is the required answer
        Y = [0 for i in range(n+1)]
        
        Y[n] = 1 # base case
        i=n-1
        while i >= 0:
            temp = 1
            for j in X.keys():
                if j != S[i]:
                    temp += X[j]
            Y[i] = (temp + Y[i+1]) % 1000000007 
            X[S[i]] = Y[i+1]
            i-=1
        
        print(Y)
        
        return (Y[0]-1) % 1000000007 
        
        
        
