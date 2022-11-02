import operator

a1="aaaa"
d1={}
def fun(prev,d):
    # res=[]
    ct=1
    for i in range(len(prev)):
        if i == len(prev) - 1 or prev[i] != prev[i + 1]:
            el  = prev[i]
            # res.append((el,ct))
            if el not in d:
                d[el] = ct
            else:
                d[el] = max(d[el],ct)

            ct = 1

        else:
            ct += 1
    # return res
    return dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
print(fun(a1,d1))
print(d1)
print(dict( sorted(d1.items(), key=operator.itemgetter(1),reverse=True)))
a2="aaab"
d2={}
print(fun(a2,d2))
print(d2)
print(dict( sorted(d2.items(), key=operator.itemgetter(1),reverse=True)))
print(d1.get('b',0))

# op
# {'a': 4}
# {'a': 4}
# {'a': 4}
# {'a': 3, 'b': 1}
# {'a': 3, 'b': 1}
# {'a': 3, 'b': 1}
# 0