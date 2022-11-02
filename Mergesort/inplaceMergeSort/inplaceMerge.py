arr = [10, 4, 234, 5, 1, 12, 55, 0, 7, 4, 4, 3, 2, 548, 1000, 332, 9, 0]


def merge(arr, s, m, e):
    l = s
    r = m
    k = 0
    newArr = [0] * (e - s)
    while l < m and r < e:
        ele_l = arr[l]
        ele_r = arr[r]

        if ele_l < ele_r:
            newArr[k] = ele_l
            l += 1
        else:
            newArr[k] = ele_r
            r += 1
        k += 1
    if l < m:
        while l < m:
            newArr[k] = arr[l]
            l += 1
            k += 1
    if r < e:
        while r < e:
            newArr[k] = arr[r]
            k += 1
            r += 1

    for e in range(len(newArr)):
        arr[s + e] = newArr[e]


def f(arr, s, e):
    if (e - s) == 1:
        return
    m = (e + s) // 2
    f(arr, s, m)
    f(arr, m, e)
    merge(arr, s, m, e)

f(arr, 0, len(arr))
print(arr)




