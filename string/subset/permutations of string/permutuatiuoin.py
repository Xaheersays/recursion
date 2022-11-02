unpro="123"

def f(pro,unpro):
    if len(unpro) == 0:
        print(pro)
        return
    ch = unpro[0]
    for i in range(len(pro)+1):
        first = pro[0:i]
        second = pro[i:]
        f(first+ch+second,unpro[1:])
print(f("",unpro))


# creating lists in body
unpro="abc"
def f(pro,unpro):
    if len(unpro) == 0:
        res = [pro]
        return res
    ch = unpro[0]
    newL=[]
    for i in range(len(pro)+1):
        first = pro[0:i]
        second = pro[i:]
        ans = f(first+ch+second,unpro[1:])
        for e in ans:
            newL.append(e)
    return sorted(newL)
print(f("",unpro))


# counting permutatioins :dumbass use factorial
unpro="abfndbabf"
def f(pro,unpro):
    cnt = 0
    if len(unpro) == 0:
        return 1
    ch = unpro[0]
    for i in range(len(pro)+1):
        first = pro[0:i]    
        second = pro[i:]
        cnt +=f(first+ch+second,unpro[1:])
    return cnt
print(f("",unpro))