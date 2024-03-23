grid=[[2,5,4],[1,5,1]]
if len(grid[0])==1:
    print(0)
else:
    arr1,arr2=[],[]
    sum1,sum2,j=0,0,len(grid[0])-1
    for i in range(len(grid[0])):
        sum1+=grid[0][j]
        sum2+=grid[1][i]
        j-=1
        arr1.insert(0,sum1)
        arr2.append(sum2)
    m1=arr1[1]
    m2=0
    gr=m1
    for i in range(1,len(grid[0])):
        if i==len(grid[0])-1:
            if arr2[i-1]<gr:
                m1=0
                m2=arr2[i-1]
                gr=m2
            continue
        if arr1[i+1]<gr and arr2[i-1]<gr:
            m1=arr1[i+1]
            m2=arr2[i-1]
            if m1>m2:
                gr=m1
            else:
                gr=m2
    print(gr)