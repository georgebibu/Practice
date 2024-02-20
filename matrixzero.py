matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
zero=[]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j]==0:
            zero.append([i,j])
for i in zero:
    for j in range(len(matrix)):
        matrix[j][i[1]]=0
    for j in range(len(matrix[0])):
        matrix[i[0]][j]=0
print(matrix)