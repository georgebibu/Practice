n=int(input("Enter length of list:"))
list=[]
alist=[]
done=[]
for i in range(n):
    x=input("Enter string:")
    list.append(x)
for i in range(n):
    if list[i] in done:
        continue
    alist.append(list[i])
    for j in range(i+1,n):
        str=list[i]
        flag=0
        for x in list[j]:
            if x in str:
                str=str.replace(x,'',1)
            else:
               flag=1
        if flag==0:
            alist.append(list[j])
            done.append(list[j])
    print(alist)
    alist.clear()
    done.append(list[i])