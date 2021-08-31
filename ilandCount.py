"""Here we've given a 2D array grid containing L and W(land and water) and we need to return count of ilands"""

def ilandCount(grid):
    visited=set()
    count=0
    for r in range(0,len(grid)):
        for c in range(0,len(grid[0])):
            #here we need a helper function to explore the grid
           if(explore(grid,r,c,visited)):
               count+=1
    return count

def explore(grid,r,c,visited):
    rowInbound=0 <=r and r < len(grid)
    colInbound=0 <=c and c  < len(grid[0])
    if(not(rowInbound) or not(colInbound)):return False

    if(grid[r][c]=='W'):return False
    #we add the position in the visited in the form of string
    position=str(r)+','+str(c)

    if(position in visited): return False
    visited.add(position)

    explore(grid,r-1,c,visited)
    explore(grid,r+1,c,visited)
    explore(grid,r,c-1,visited)
    explore(grid,r,c+1,visited)

    return True

grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

print(ilandCount(grid))