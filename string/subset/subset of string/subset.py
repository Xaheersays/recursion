s= "abc"

def subsequneces(sub,unpro):
    if len(unpro)==0:
        print(sub)
        return
    ch = unpro[0]
    subsequneces(sub,unpro[1:])
    subsequneces(sub+ch,unpro[1:])

(subsequneces("",s))    