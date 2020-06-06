# 882. Reachable Nodes in a Subdivided Graph

import heapq

class Solution:
   
    def Dijkstras(self, G, M):
        final_distances = {}
        marked = {}
       
        li = []
        heapq.heapify(li)
       
        heapq.heappush(li, (0, 0))
       
        while len(li) > 0:
            dist,node = heapq.heappop(li)
            if dist > M:
                break
            if node not in final_distances:
                for neighbor in G[node]:
                    if neighbor not in marked:
                        marked[neighbor] = dist + G[node][neighbor]
                        heapq.heappush(li,(marked[neighbor], neighbor))
                    else:
                        if dist + G[node][neighbor] < marked[neighbor]:
                            marked[neighbor] = dist + G[node][neighbor]
                            heapq.heappush(li, (marked[neighbor], neighbor))
                final_distances[node] = dist
        return final_distances
   
    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        G = {}
        for edge in edges:
            node1, node2, weight = edge[0], edge[1], edge[2]+1
            if node1 not in G:
                G[node1] = {}
            if node2 not in G:
                G[node2] = {}
            G[node1][node2] = weight
            G[node2][node1] = weight
       
        if 0 not in G:
            return 1
       
        distances = self.Dijkstras(G, M)
       
        count = 0
        for edge in edges:
            node1, node2, weight = edge[0], edge[1], edge[2]
            if node1 in distances and node2 in distances:
                count += min(2*M-distances[node1]-distances[node2], weight)
            elif node1 in distances:
                count += M-distances[node1]
            elif node2 in distances:
                count += M-distances[node2]
        return count + len(distances)
