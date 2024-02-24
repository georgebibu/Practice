n=float(input("Enter number:"))
p=int(input("Enter power:"))
res=1.0
if p<0:
    for i in range(-p):
        res=res/n
else:
    for i in range(p):
        res=res*n
print(res)