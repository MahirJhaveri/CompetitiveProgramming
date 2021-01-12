# Problem 85 - Maximal Rectangle

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        H = len(matrix)
        if H == 0:
            return 0
        
        W = len(matrix[0])
        
        f = [0 for x in range(W)]
        
        ans = 0
        
        r = 0
        while r < H:
            c = 0
            stack = []
            while c < W:
                f[c] = f[c]+1 if matrix[r][c] == "1" else 0
                temp = c
                while len(stack) > 0 and stack[-1][0] > f[c]:
                    (h, i) = stack.pop()
                    temp = i
                    ans = max(ans, h*(c-i))
                stack.append((f[c], temp))
                c += 1
            while len(stack) > 0:
                (h, i) = stack.pop()
                ans = max(ans, h*(c-i))
            r += 1
        
        return ans
        
