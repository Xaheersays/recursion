
def f(row,col):
    if row ==1 or col ==1:
        return  1
    down = f(row-1,col)
    right  = f(row,col-1)
    return down+right

print(f(4,5))