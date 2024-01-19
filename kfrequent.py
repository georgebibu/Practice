k=int(input("Enter frequency:"))
dict={}
list=[]
out=[]
n=int(input("Enter length of list:"))
for i in range(n):
    x=int(input("Enter integer:"))
    list.append(x)
for i in list:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]=dict[i]+1
    if i not in out and dict[i]>=k:
        out.append(i)
print(out)
    