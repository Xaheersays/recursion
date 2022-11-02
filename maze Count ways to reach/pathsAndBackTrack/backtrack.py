grid = [[1,1,1],[1,1,1],[1,1,1]]
def pathInArrayAndBackTrack(pro,row,col,grid):
    res = []
    if row == len(grid)-1 and  col == len(grid)-1:
        res.append(pro)
        return res
    if not grid[row][col]:          #doing this here becoz we are marking cell false
        return []
    grid[row][col]=0
    if row < len(grid)-1  :
        DOWN =pathInArrayAndBackTrack(pro+"D",row+1,col,grid)
        for e in DOWN:
            res.append(e)
    if  col < len(grid)-1 :
        RIGHT = pathInArrayAndBackTrack(pro+"R",row,col+1,grid)
        for e in RIGHT:
            res.append(e)
    if row>0:
        UP = pathInArrayAndBackTrack(pro+"U",row-1,col,grid)
        for e in UP:
            res.append(e)
    if col > 0:
        BOTTOM = pathInArrayAndBackTrack(pro+"B",row,col-1,grid)
        for e in BOTTOM:
            res.append(e)
    grid[row][col]=1            #revertig my changes (backtrack)
    return res
print(pathInArrayAndBackTrack("",0,0,grid))
