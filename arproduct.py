n=int(input("Enter length of array:"))
inp=[]
pre=[1]
post=[1]
out=[]
for i in range(n):
    x=int(input("Enter element:"))
    inp.append(x)
    pre.append(1)
    post.append(1)
    out.append(1)
for i in range(1,n+1):
     pre[i]=inp[i-1]*pre[i-1]
     post[n-i]=inp[n-i]*post[n-i+1]
for i in range(n):
     out[i]=pre[i]*post[i+1]
print(out)