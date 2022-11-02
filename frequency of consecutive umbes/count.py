# from collections import Counter
# arr="aaaa"

def fun(prev):
    res=[]
    ct= 1
    for i in range(len(prev)):
        if i == len(prev) - 1 or prev[i] != prev[i + 1]:
            res.append((prev[i],ct))
            ct = 1
        else:
            ct += 1
    return res
print(fun("wwdl"))


# def solve(arr):
#     ans = fun(arr)
#     print(ans)
#     cnt = 0
#     for ele in ans:
#         if ele > 1:
#             cnt+=1
#     return cnt
#
#
#
# def f(arr):
#     n = len(arr)
#     res = []
#     i = 0
#     while i < n :
#         cnt = 1
#         while i < n-1 and arr[i] == arr[i + 1]:
#             cnt += 1
#             i = i + 1
#         res.append((arr[i],cnt))
#         res.append(cnt)
#         i = i + 1
#     return res
#
# d1=f(arr)
# arr1="aaab"
# d2=f(arr1)
#
# d = Counter(d1)
# print(d)
# i = Counter(d2)
# print(i)


# print(f(arr, len(arr)))

