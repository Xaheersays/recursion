def pathInArray(pro,row,col):
    res = []
    if row ==1 and col ==1:
        res.append(pro)
        return res

    if row>1:
        left = (pathInArray(pro+"d",row-1,col))
        for e in left:
            res.append(e)
    if col >1:
        right =(pathInArray(pro+"r",row,col-1))
        for e in right:
            res.append(e)
    return res
print(pathInArray("",5,5))
