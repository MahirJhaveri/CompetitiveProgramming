# Problem 1766 - Tree of Coprimes

import math

def aux(i, G, ans, nums, r, prev, d):
    ans[i]=-1
    ans_depth = -1
    for j in range(1,51):
        if gcd(j, nums[i]) == 1:
            if r[j][0] > ans_depth:
                ans_depth = r[j][0]
                ans[i]=r[j][1]
    temp = r[nums[i]]
    r[nums[i]] = [d, i]
    for n in G[i]:
        if n != prev:
            aux(n,G,ans,nums,r,i,d+1)
    r[nums[i]]=temp

class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        
        G = {0:[]}
        for [u,v] in edges:
            if u not in G:
                G[u] = []
            if v not in G:
                G[v] = []
            G[u].append(v)
            G[v].append(u)
        
        ans = [0 for i in range(len(nums))]
        aux(0, G, ans, nums, [[-1,-1] for _ in range(51)], None, 0)
        return ans
        
