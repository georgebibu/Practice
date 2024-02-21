matrix=[[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
sum=0
if len(matrix)%2==0:
    for i in range(len(matrix)):
        sum+=matrix[i][i]
else:
    for i in range(len(matrix)):
        if i==len(matrix)//2:
            continue
        else:
            sum+=matrix[i][i]
i=0
for j in range(len(matrix)-1,-1,-1):
    sum+=matrix[i][j]
    i+=1
print(sum)