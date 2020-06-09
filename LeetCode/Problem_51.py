# Problem 51: N-Queens

class Solution:
   
   
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        ans = []
        pos = []
        aux(n, pos, ans, result, 0)
        return result
       
def aux(n, pos, ans, result, row):
    for col in range(n):
        temp = True
        for (row2, col2) in pos:
            if col == col2 or abs(row2 - row) == abs(col - col2):
                temp = False
        if temp:
            if row < n-1:
                pos.append((row, col))
                temp = ""
                for i in range(n):
                    temp += "." if not i == col else "Q"
                ans.append(temp)
                aux(n, pos, ans, result, row+1)
                ans.pop()
                pos.pop()
            else:
                temp = ""
                for i in range(n):
                    temp += "." if not i == col else "Q"
                ans.append(temp)
                result.append(ans.copy())
                ans.pop()
