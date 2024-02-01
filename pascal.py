x=int(input("Enter number of rows:"))
p=0
out=[]
for i in range(x):
    if i==0:
        out.append([1])
    elif i==1:
        out.append([1,1])
        p+=1
    else:
        temp=[1]
        for j in range(len(out[p])-1):
            temp.append(out[p][j]+out[p][j+1])
        temp.append(1)
        out.append(temp)
        p+=1
print(out)