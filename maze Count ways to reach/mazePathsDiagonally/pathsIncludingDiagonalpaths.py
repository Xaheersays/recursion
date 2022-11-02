def pathsDiagonally(pro,row,col):
    res = []
    if row ==1 and col ==1:
        res.append(pro)
        return res

    if row>1:
        left = pathsDiagonally(pro+"b",row-1,col)
        for e in left:
            res.append(e)
    if col >1:
        right =pathsDiagonally(pro+"r",row,col-1)
        for e in right:
            res.append(e)
    if row > 1 and col > 1:
        diagonal  = pathsDiagonally(pro+"d",row-1,col-1)
        for d in diagonal:
            res.append(d)
    return res

print(pathsDiagonally("",3,3))