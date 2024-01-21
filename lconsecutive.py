n=int(input("Enter length:"))
c=1
l=1
list=[]
for i in range(n):
    x=int(input("Enter element:"))
    list.append(x)
list.sort()
for i in range(i):
    if list[i]+1==list[i+1]:
        c+=1
        if c>l:
            l=c
    else:
        c=1
print("Length of longest consecutive numbers in the list is ",l)