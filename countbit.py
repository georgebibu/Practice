n=10
list=[]
for i in range(n+1):
    count=0
    while i>0:
        if i%2==1:
            count+=1
        i=i//2
    list.append(count)
print(list)