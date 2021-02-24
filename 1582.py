matrix=[[0,0,0,0,0],
        [1,0,0,0,0],
        [0,1,0,0,0],
        [0,0,1,0,0],
        [0,0,0,1,1]]

result=0
x=0
loc=0
for i in range(len(matrix)):
    x=0
    for j in  range(len(matrix[i])):
        if matrix[i][j]==1:
            x+=1
            loc=j
    if x==1:
        for k in range(len(matrix)):
            if matrix[k][loc]==1 and i!=k:
                x+=1
    if x==1:
        result+=1

print(result)