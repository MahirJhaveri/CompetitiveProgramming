class Solution(object):
    
    def numIslands(self, grid):
        count=0
        numrows=len(grid)
        
        if numrows == 0:
            return 0
        
        numcols=len(grid[0])
        
        row=0
        while row<numrows:
            col=0
            while col<numcols:
                if grid[row][col] == "1":
                    count+=1
                    mark(row,col,numrows,numcols,grid)
                col+=1
            row+=1
        return count

def mark(r,c, numrows, numcols, grid):
    grid[r][c]='*'
    if r>0 and grid[r-1][c]=='1':
        mark(r-1,c,numrows,numcols,grid)
    if r<numrows-1 and grid[r+1][c]=='1':
        mark(r+1,c,numrows,numcols,grid)
    if c>0 and grid[r][c-1]=='1':
        mark(r,c-1,numrows,numcols,grid)
    if c<numcols-1 and grid[r][c+1]=='1':
        mark(r,c+1,numrows,numcols,grid)
    return
