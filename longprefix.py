strs=list(map(str,input("Enter strs:").split()))
res,flag,min="",0,201
for i in strs:
    if len(i)<min:
        min=len(i)
for i in range(min):
    for j in strs:
        if j[i]!=strs[0][i]:
            flag=1
            break
    if flag==0:
        res+=strs[0][i]
print(res)