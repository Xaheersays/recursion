arr=[1,2,3]
def f(arr):
    outer = [[]]
    for num in arr:
        for i in range(len(outer)):
            outer.append(outer[i]+[num])
    return outer
print(f(arr))