# Problem 207: Course Schedule

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True
       
        # first generate a graph
        G={}
        for [pre, post] in prerequisites:
            if pre not in G:
                G[pre] = {}
            if post not in G:
                G[post] = {}
            G[pre][post] = -1
       
        vertices = list(G.keys())
       
        ans = True
       
        i=0
        marked = {}
        while i < len(vertices):
            if vertices[i] in G and vertices[i] not in marked:
                ans = ans and dfs(vertices[i], G, marked, {})
            i += 1
        return ans
       
def dfs(node, G, marked, processing):
    if node in processing and processing[node]:
        return False
    elif node in marked and marked[node]:
        return True
    else:
        processing[node] = True
        ans = True
        for v in G[node]:
            ans = ans and dfs(v, G, marked, processing)
        processing[node] = False
        marked[node] = True
        return ans
