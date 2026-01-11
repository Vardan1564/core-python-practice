# --------------recursion-------------
def f1(n):
    if n==1:
        return 1
    return n**2+f1(n-1)
x=f1(2)
print(x)