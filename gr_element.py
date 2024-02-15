n=int(input("Enter number of elements:"))
gr,a=0,[]
for i in range(n):
    x=int(input("Enter element:"))
    a.append(x)
for i in range(0,len(a)):
    if i==len(a)-1:
        a[i]=-1
    else:
        gr=a[i+1]
        for j in range(i+1,len(a)):
            if a[j]>gr:
                gr=a[j]
        a[i]=gr
print(a)