def check(a,b):
    a.sort()
    flag=0
    for i in b:
        i.sort()
    if a in b:
        flag=1
    if flag==0:
        b.append(a)
n=int(input("Enter number of elements:"))
list=[]
out=[]
temp=[]
for i in range(n):
    x=int(input("Enter element:"))
    list.append(x)
for i in range(n):
    j=(i+1)%n
    while j!=i:
        flag=0
        k=(j+1)%n
        while k!=i:
            if list[j]+list[k]==-list[i]:
                temp.append(list[i])
                temp.append(list[j])
                temp.append(list[k])
                flag=1
                break
            k=(k+1)%n
        if flag==1:
            check(temp,out)
            temp=[]
        j=(j+1)%n
print(out)     