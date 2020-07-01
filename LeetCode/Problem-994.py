# problem 994: Rotten Oranges

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
       
        new_grid = []
        count = 0
       
        def neighbors(pos):
            result = []
            if pos[0] > 0:
                result.append((pos[0]-1, pos[1]))
            if pos[0] < rows-1:
                result.append((pos[0]+1, pos[1]))
            if pos[1] > 0:
                result.append((pos[0],pos[1]-1))
            if pos[1]< cols-1:
                result.append((pos[0],pos[1]+1))
            return result
       
        # first find every single possible starting orange (rotten at start)
        start_pos = []
        for r in range(rows):
            new_grid.append([])
            for c in range(cols):
                if grid[r][c] == 2:
                    start_pos.append((r,c))
                    new_grid[r].append(0)
                elif grid[r][c] == 1:
                    count += 1
                    new_grid[r].append(10000000000)
                else:
                    new_grid[r].append(0)
       
        for p in start_pos:
            stack = [p]
            while len(stack) > 0:
                pos = stack.pop()
                for npos in neighbors(pos):
                    if grid[npos[0]][npos[1]] == 1:
                        count -= 1
                        grid[npos[0]][npos[1]] = 2
                        stack.append(npos)
                        new_grid[npos[0]][npos[1]] = new_grid[pos[0]][pos[1]] + 1
                    elif grid[npos[0]][npos[1]] == 2:
                        if new_grid[npos[0]][npos[1]] > new_grid[pos[0]][pos[1]] + 1:
                            new_grid[npos[0]][npos[1]] = new_grid[pos[0]][pos[1]] + 1
                            stack.append(npos)
       
       
        if count > 0:
            return -1
        else:
            ans = -1
            for r in range(rows):
                for c in range(cols):
                    ans = ans if ans >= new_grid[r][c] else new_grid[r][c]
            return ans
