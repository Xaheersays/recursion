grid = [
    [1,1,1,1],
    [1,0,0,1],
    [1,0,1,1],
    [1,1,0,1]
]
# going from end to 0
def pathInArray(pro,row,col,grid):
    res = []
    if row ==0 and col ==0:
        res.append(pro)
        return res
    if not grid[row][col]:
        return []
    if row>0:
        left = (pathInArray(pro+"d",row-1,col,grid))
        for e in left:
            res.append(e)
    if col >0 :
        right =(pathInArray(pro+"r",row,col-1,grid))
        for e in right:
            res.append(e)
    return res
print(pathInArray("",3,3,grid))



# alternative using river condition with row and col itself
# grid = [[1,1,1],[1,0,1],[1,1,1]]
def pathInArrayAlternative(pro,row,col,grid):
    res = []
    if row ==0 and col ==0:
        res.append(pro)
        return res
    # if not grid[row][col]:
    #     return []
    if row>0 and grid[row][col]:
        left = (pathInArrayAlternative(pro+"d",row-1,col,grid))
        for e in left:
            res.append(e)
    if col >0 and grid[row][col] :
        right =(pathInArrayAlternative(pro+"r",row,col-1,grid))
        for e in right:
            res.append(e)
    return res
print(pathInArrayAlternative("",len(grid)-1,len(grid)-1,grid))

# <-------------------------------------------------------------------------------------------------->

# going from zero to end

def pathInArray0toEnd(pro,row,col,grid):
    res = []
    if row == len(grid)-1 and  col == len(grid)-1:
        res.append(pro)
        return res

    if row < len(grid)-1 and grid[row][col]:
        left =pathInArray0toEnd(pro+"d",row+1,col,grid)
        for e in left:
            res.append(e)
    if  col < len(grid)-1 and grid[row][col]:
        right = pathInArray0toEnd(pro+"r",row,col+1,grid)
        for e in right:
            res.append(e)
    return res
print(pathInArray0toEnd("",0,0,grid))

def pathInArray0toEndAlternative(pro,row,col,grid):
    res = []
    if row == len(grid)-1 and  col == len(grid)-1:
        res.append(pro)
        return res

    if not grid[row][col]:
        return []

    if row < len(grid)-1 :
        left =pathInArray0toEndAlternative(pro+"d",row+1,col,grid)
        for e in left:
            res.append(e)
    if  col < len(grid)-1 :
        right = pathInArray0toEndAlternative(pro+"r",row,col+1,grid)
        for e in right:
            res.append(e)
    return res
print(pathInArray0toEndAlternative("",0,0,grid))