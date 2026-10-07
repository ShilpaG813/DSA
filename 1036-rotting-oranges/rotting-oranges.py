from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        rows=len(grid)
        cols=len(grid[0])
        queue=deque()
        fresh=0
        for i in range(rows):
            for j in range(cols):
                if(grid[i][j]==2):
                    queue.append((i,j))
                elif(grid[i][j]==1):
                    fresh+=1
        min=0
        while queue and fresh>0:
            for _ in range(len(queue)):
                i,j=queue.popleft()
                if i>0 and grid[i-1][j]==1:
                    grid[i-1][j]=2
                    fresh-=1
                    queue.append((i-1,j))
                if i<rows-1 and grid[i+1][j]==1:
                    grid[i+1][j]=2
                    fresh-=1
                    queue.append((i+1,j))
                if j>0 and grid[i][j-1]==1:
                    grid[i][j-1]=2
                    fresh-=1
                    queue.append((i,j-1))
                if j<cols-1 and grid[i][j+1]==1:
                    grid[i][j+1]=2
                    fresh-=1
                    queue.append((i,j+1))
            min+=1
        if fresh==0:
            return min
        else:
            return -1
        