# Problem 1499: Max Value of Equation
import heapq

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        h = []
        heapq.heapify(h)
        ans = -1000000000000
        i=0
        while i<len(points):
            xj, yj = points[i][0], points[i][1]
            if len(h) > 0:
                diff, xi = -1*h[0][0], h[0][1]
                while xj-xi > k and len(h)>1:
                    heapq.heappop(h)
                    diff, xi = -1*h[0][0], h[0][1]
                if xj-xi <= k:
                    if ans < diff + xj + yj:
                        ans = diff + xj + yj
            heapq.heappush(h, (-points[i][1]+points[i][0], points[i][0]))
            i+=1
        return ans
