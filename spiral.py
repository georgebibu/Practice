matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
res=[]
r=len(matrix)
c=len(matrix[0])
if r==1:
    for i in range(c):
        res.append(matrix[0][i])
    print(res)
if c==1:
    for i in range(r):
        res.append(matrix[i][0])
    print(res)
n=r*c
dir=0
i,j=0,1
start=(0,0)
left=0
res=[matrix[0][0]]
for k in range(n-1):
    res.append(matrix[i][j])
    if r-left==1:
        dir=0
        j+=1
        continue
    elif c-left==1:
        dir=1
        i+=1
        continue
    else:
        if (i,j)==(r-1,c-1) or (i,j)==(left,c-1) or (i,j)==(r-1,left):
            dir=(dir+1)%4
    if (i-1,j)==start:
        dir=0
        j+=1
        start=(i,j)
        r-=1
        c-=1
        left+=1
    elif dir==0:
        j+=1
    elif dir==1:
        i+=1
    elif dir==2:
        j-=1
    else:
        i-=1
print(res)