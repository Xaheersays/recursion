def path(pro,row,col):
    if row == 1 and col ==1 :
        print(pro)
        return
    if row>1:
        path(pro+"d",row-1,col)
    if col>1:
        path(pro+"r",row,col-1)
path("",2,2)