nums = 16
def Check(n,nums,cnt):
    if cnt > 2 or n > nums :
        return cnt
    if  nums%n == 0:
        return Check(n+1,nums,cnt+1)
    else:
        return Check(n+1,nums,cnt)
ans =Check(1,nums,0)

if ans >=3:
    print(f"{nums} is not prime")
else:
    print(f"{nums} is prime ")