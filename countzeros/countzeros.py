n = 200930293092000000000000000000000000000000000000000000000000000000000000000000000000000009302903920000230
def CountZeros(n, cnt):
    if n % 10 == n:
        return cnt
    if n % 10 == 0:
        return CountZeros(n // 10, cnt + 1)
    else:
        return CountZeros(n // 10, cnt)
print(CountZeros(n, 0))


# n  = 20230

def CountZeros1(n,cnt):
    if n == 0:
        return cnt
    rem  =  n%10
    if rem == 0:
        return CountZeros1(n//10 , cnt+1)
    return CountZeros1(n//10 , cnt)

print(CountZeros1(n,0))