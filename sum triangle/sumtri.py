arr = [1, 2, 3, 4, 5]

def help(newArr, i, arr):
    if i == len(newArr):
        return
    newArr[i] = arr[i] + arr[i + 1]
    help(newArr, i + 1, arr)

def f(arr):
    if len(arr) == 1:
        return
    newArr = [0] * (len(arr) - 1)
    help(newArr, 0, arr)
    f(newArr)
    print(newArr)

f(arr)
print(arr)