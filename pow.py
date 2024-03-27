x=2
n=5
if n==0:
    print(1)
if x==0:
    print(0)
res=1
if n<0:
    n=-n
    x=1/x
    while n>0:
        if n%2==0:
            x=x*x
            n=n/2
        else:
            res=res*x
            n-=1
else:
    while n>0:
        if n%2==0:
            x=x*x
            n=n/2
        else:
            res=res*x
            n-=1
print(res)