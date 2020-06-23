# Problem 790: Domino and Tromino Tiling

class Solution:
    def numTilings(self, N: int) -> int:
        ftable = [1,1]
        gtable = [0]
       
        if N < 2:
            return N
       
        n=2
        while n<=N:
            fn = (ftable[1]+ftable[0]+2*gtable[0])%1000000007
            gn = (ftable[0]+gtable[0])%1000000007
            ftable[0]=ftable[1]
            ftable[1]=fn
            gtable[0]=gn
            n+=1
        return ftable[1]
