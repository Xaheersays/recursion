def fun(prev):
    res=[]
    ct=1
    for i in range(len(prev)):
        if i == len(prev) - 1 or prev[i] != prev[i + 1]:
            res.append(ct)
            ct = 1
        else:
            ct += 1
    return res

def solve(arr):
    ans = fun(arr)
    cnt = 0
    for ele in ans:
        if ele>1:
            cnt= cnt + ele -1
    return cnt


if __name__=="__main__":
    t = int(input())
    for i in range(t):
        arr = list(map(int,input().split()))
        print(solve(arr))