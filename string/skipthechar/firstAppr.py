upr= "absndbaasndsvvachvsdahcdhavbnaccaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaanaaamhds"
def f(upr):
    ans = ''
    if len(upr) == 0:
        return ans
    ch = upr[0]
    if ch == 'a':
        res = f(upr[1:]) #why res becoz
    else:
        ans+=ch
        res = f(upr[1:])
    if res:
        ans+=res
    return ans
print(f(upr))

# 1 => ek to neeche se collect krte jaao strings
# 2 => ek parameter hi bhej do ans collect krne ke liye
