# Problem 1468C - Berpizza

import heapq
from collections import deque

queue = deque()
heap = []
hmap = {}

def process_new_client(I, m):
    queue.append(I)
    heapq.heappush(heap, (-1*m ,I))

# monocarp serves client
def served_by_1():
    res = None
    while True:
        res = queue.popleft()
        if res not in hmap:
            break
    hmap[res] = True
    return res

#ploycarp serves client
def served_by_2():
    res = None
    while True:
        res = heapq.heappop(heap)
        if res[1] not in hmap:
            break
    hmap[res[1]] = True
    return res[1]

def main():
    Q = int(input())
    I = 1
    for c in range(Q):
        inp = input().rstrip().split(" ")
        if len(inp) == 2:
            process_new_client(I, int(inp[1]))
            I += 1
        else:
            if inp[0] == "2":
                res = served_by_1()
                print(res)
            else: # type 3 query
                res = served_by_2()
                print(res)

main()
