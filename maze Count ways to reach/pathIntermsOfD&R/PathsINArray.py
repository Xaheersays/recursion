res= []
def pathInArray(pro,row,col,res):
    if row ==1 and col ==1:
        res.append(pro)
        return
    if row>1:
        pathInArray(pro+"d",row-1,col,res)
    if col >1:
        pathInArray(pro+"r",row,col-1,res)

pathInArray("",3,3,res)
print(res)