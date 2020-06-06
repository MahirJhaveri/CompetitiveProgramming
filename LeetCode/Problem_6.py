# 6. ZigZag Coversion
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        jmp = (numRows) + (numRows-1) -1
        ans=""
        row=0
        while row<numRows:
            i=0
            while i<len(s):
                if i%jmp == row or (jmp - (i%jmp)) == row:
                    ans += s[i]
                i+=1
            row+=1
        return ans
