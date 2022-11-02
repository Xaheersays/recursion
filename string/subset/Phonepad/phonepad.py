unpro="12"
def f(pro,unpro):
    cnt = 0
    if len(unpro) == 0:
        print(pro)
        return
    digit = int(unpro[0])
    for i in range((digit-1)*3,digit*3):
        ch = chr(i+97)
        f(pro+ch,unpro[1:])
print(f("",unpro))