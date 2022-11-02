"""
sum = 4 + f(838)                                                                return to main 4+19
                -> 8 + f(83)                                               return 8+11
                    |-> 3 + f(8)                                return 3+8
                            |-> 8 + f(0)                return 8+0
                                    |-> f(0)= 0 return 0
          
          
        4 ==> n%10 
        f(838) ==> n//10     8384//10 ==> 838

"""
n=8384
def sumOfDigits(n):
    if n == 0 :
        return  0
    return   n%10  + sumOfDigits(n//10)
print(sumOfDigits(8384))

def f(n):
    s = 0
    while n:
        s += n%10
        n = n//10
    print(s)
f(n)

ans = 1e12+1
print(int(ans//1000))