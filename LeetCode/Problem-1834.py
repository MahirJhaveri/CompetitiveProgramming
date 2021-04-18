# Problem 1834 - Single Threaded CPU

import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [[tasks[i][0], tasks[i][1], i] for i in range(len(tasks))]
        tasks.sort(key=lambda tup: tup[0])
        ans = []
        curr_time = 0
        h = []
        heapq.heapify(h)
        i=0
        while i < len(tasks):
            while len(h)>0 and curr_time < tasks[i][0]:
                (delta, index) = heapq.heappop(h)
                curr_time += delta
                ans.append(index)
            curr_time = max(curr_time, tasks[i][0])
            j = i
            while j < len(tasks) and tasks[j][0] <= curr_time:
                heapq.heappush(h, (tasks[j][1], tasks[j][2]))
                j += 1
            i = j
        while len(h)>0:
            (delta, index) = heapq.heappop(h)
            curr_time += delta
            ans.append(index)
        return ans
        
