a=input("Enter a:")
b=input("Enter b:")
c=0
res=""
if len(a)>=len(b):
    for i in range(len(a)-len(b)):
        b="0"+b
else:
    for i in range(len(b)-len(a)):
        a="0"+a
print(a,b)
for i in range(len(a)-1,-1,-1):
    if c==0:
        if a[i]=='0' and b[i]=='0':
            res="0"+res
            c=0
        elif a[i]=='1' and b[i]=='1':
            res="0"+res
            c=1
        else:
            res="1"+res
            c=0
    else:
        if a[i]=='0' and b[i]=='0':
            res="1"+res
            c=0
        elif a[i]=='1' and b[i]=='1':
            res="1"+res
            c=1
        else:
            res="0"+res
            c=1
if(c==1):
    res="1"+res
print(res)      