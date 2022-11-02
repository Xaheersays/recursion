arr = [10, 4, 234, 5, 1, 12, 55, 0, 7, 4, 4, 3, 2, 548, 1000, 332, 9, 0]

def f(arr,lo,hi):
    if lo >= hi:
        return
    s = lo
    e = hi
    mid = (s+e)//2
    pivot = arr[mid]
    while s<=e:
        while arr[s] < pivot :
            s+=1
        while arr[e] > pivot :
            e-=1
        if s<=e: #stoping to swap those values which are already sorted
            arr[s],arr[e]=arr[e],arr[s]
            s+=1
            e-=1
    f(arr,lo,e)
    f(arr,s,hi)
print(f(arr,0,len(arr)-1))
print(arr)
