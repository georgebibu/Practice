n=int(input("Enter length:"))
list=[]
for i in range(n):
    x=int(input("Enter color number:"))
    list.append(x)
for i in range(n):
    for j in range(i+1,n):
        if list[i]>list[j]:
            temp=list[i]
            list[i]=list[j]
            list[j]=temp
print(list)
