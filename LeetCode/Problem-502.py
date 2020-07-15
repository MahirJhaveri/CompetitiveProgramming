# Problem 502 : IPO
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        # store activites in order of dec P having C below a certain threshold
        h = []
        heapq.heapify(h)
       
        # store activities in order of dec C having C above a certain threshold
        l = []
       
        for i in range(len(Profits)):
            if Capital[i]<=W:
                heapq.heappush(h,-1*Profits[i])
            else:
                l.append((Capital[i],Profits[i]))
       
        l.sort(key=lambda tup: tup[0], reverse=True)
       
       
        n=0
        while len(h)>0 and n<k:
            W += -1*heapq.heappop(h)
            while len(l)>0 and l[-1][0] <= W:
                heapq.heappush(h,l[-1][1]*-1)
                l.pop()
            n+=1
        return W
