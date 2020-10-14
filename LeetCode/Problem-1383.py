# Problem 1383 - Maximum Performance of a Team

import heapq

class Solution(object):
    def maxPerformance(self, n, speed, efficiency, k):
        """
        :type n: int
        :type speed: List[int]
        :type efficiency: List[int]
        :type k: int
        :rtype: int
        """
        combined = zip(efficiency, speed)
        combined.sort(key = lambda tup: tup[0], reverse = True)
        
        # create a min heap
        pq = []
        heapq.heapify(pq)
        
        s = 0
        i = 0
        ans = 0
        while i < k:
            s += combined[i][1]
            heapq.heappush(pq, combined[i][1])
            ans = max(ans, s*combined[i][0])
            i += 1
        
        while i < len(combined):
            s += combined[i][1]
            heapq.heappush(pq, combined[i][1])
            s -= heapq.heappop(pq)
            ans = max(ans, s*combined[i][0])
            i+=1
        return ans % 1000000007
