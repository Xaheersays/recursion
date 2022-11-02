n=10
def f(n):
    if n<1:
        return
    print(n)
    f(n-1)
    print(n)
f(n)