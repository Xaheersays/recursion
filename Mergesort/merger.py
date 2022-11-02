arr = [10, 4, 234, 5, 1, 12, 55, 0, 7, 4, 4, 3, 2, 548, 1000, 332, 9, 0]


def Merge(left, right):
    l = 0
    r = 0
    size_l = len(left)
    size_r = len(right)
    newArr = [0] * (size_l + size_r)
    i = 0
    while l < size_l and r < size_r:
        ele_l = left[l]
        ele_r = right[r]

        if ele_l < ele_r:
            newArr[i] = ele_l
            l += 1
            i += 1

        else:
            newArr[i] = ele_r
            r += 1
            i += 1
    if l < size_l:
        while l < size_l:
            newArr[i] = left[l]
            i += 1
            l += 1
    if r < size_r:
        while r < size_r:
            newArr[i] = right[r]
            i += 1
            r += 1
    return newArr


def f(arr):
    size = len(arr)
    if size == 1:
        return arr
    n = size // 2
    left = f(arr[:n])
    right = f(arr[n:])
    return Merge(left, right)


print(f(arr))