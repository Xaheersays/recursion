s= "abc"
def subsequneces(sub,unpro):
    res = []
    if len(unpro)==0:
        res.append(sub)
        return res
    ch = unpro[0]
    ans_l = subsequneces(sub,unpro[1:])
    ans_r = subsequneces(sub+ch,unpro[1:])
    new = []
    # new.append(ans_l)
    # new.append(ans_r)
    if ans_l:
        for i in ans_l:
            new.append(i)
    if ans_r:
        for e in ans_r:
            new.append(e)
    return new
print(subsequneces("",s))

# removing empty sub str
s= "abc"
def subsequneces(sub,unpro):
    res = []
    if len(unpro)==0:
        res.append(sub)
        if sub=="":return []
        return res
    ch = unpro[0]
    ans_l = subsequneces(sub,unpro[1:])
    ans_r = subsequneces(sub+ch,unpro[1:])
    new = []
    # new.append(ans_l)
    # new.append(ans_r)
    if ans_l:
        for i in ans_l:
            new.append(i)
    if ans_r:
        for e in ans_r:
            new.append(e)
    new.sort()
    return  new
print(subsequneces("",s))