"""This problem also bound with the grid and we need to return the minimum no of node or point of an iland"""
import sys

def minimumIland(grid):
    visited=set()
    count=0
    minSize=sys.maxsize
    for r in range(0,len(grid)):
        for c in range(0,len(grid[0])):
            count=explore(grid,r,c,visited)
            if(count>0 and count<minSize):
                minSize=count
    return minSize
                

def explore(grid,r,c,visited):
    rowBound=0 <=r and r<len(grid)
    colBound=0 <=c and c<len(grid[0])
    if(not(rowBound) or not(colBound)):return 0

    if(grid[r][c]=='W'):return 0

    path=str(r)+','+str(c)
  
    if(path in visited): return 0
    visited.add(path)

    
    Count=1
    Count+=explore(grid,r-1,c,visited)
    Count+=explore(grid,r+1,c,visited)
    Count+=explore(grid,r,c-1,visited)
    Count+=explore(grid,r,c+1,visited)

    return Count



grid=[
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

print(minimumIland(grid))