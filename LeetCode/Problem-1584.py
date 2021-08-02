import math
# Problem 1584 - Min Cost To Connect All Points

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        points = [(u,v) for u,v in points]
        
        if len(points) == 0:
            return 0
        
        marked = {}
        shortest_dist_to_point = {}
        point = points[0]
        marked[point] = True
        for p in points:
            if p not in marked:
                shortest_dist_to_point[p] = abs(point[0]-p[0])+abs(point[1]-p[1])
                
        
        ans = 0
        
        while len(marked) < len(points):
            d = math.inf
            newpoint = None
            for p in points:
                if p not in marked and shortest_dist_to_point[p]<d:
                    d=shortest_dist_to_point[p]
                    newpoint = p
            ans += d
            marked[newpoint]=True
            point = newpoint
            for p in points:
                if p not in marked:
                    if abs(point[0]-p[0])+abs(point[1]-p[1]) < shortest_dist_to_point[p]:
                        shortest_dist_to_point[p] = abs(point[0]-p[0])+abs(point[1]-p[1])
        return ans
            
