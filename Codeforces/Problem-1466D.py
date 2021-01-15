# Problem 1466D - 13th Labour of Heracles

import heapq

def main():
    T = int(input())
    for c in range(T):
        n = int(input())
        w = input().rstrip().split(" ")
        g = [0 for i in range(n)]
        for c in range(n-1):
            inp = input().rstrip().split(" ")
            u, v = int(inp[0])-1, int(inp[1])-1
            g[u] += 1
            g[v] += 1
        heap = []
        total = 0
        for i in range(n):
            val = (int(w[i]), i, g[i])
            total += int(w[i])*g[i]
            heapq.heappush(heap, val)
        res = [str(total)]
        while len(heap) > 0:
            val = (None, None, 1)
            while len(heap) > 0 and (not (val[2] > 1)):
                val = heapq.heappop(heap)
            while val[2] > 1:
                res.append(str(int(res[-1])-val[0]))
                val = (val[0], val[1], val[2]-1)
        res = res[::-1]
        print(" ".join(res))
main()
