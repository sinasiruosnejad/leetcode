def string_to_list(string):
    x=string
    result=[]
    i=1
    while x[i]!=']':
        if x[i]!=',':
            j=i
            temp=''
            while x[j]!=',':
                if x[j]==']':
                    break
                temp+=x[j]
                j+=1
                i=j
                result.append(int(temp))
        else:
            i+=1
    return result



IN=input()
LIST=[]
temp=''
i=1
while i<len(IN):
    if IN[i]!=']':
        temp+=IN[i]
    elif IN[i]==']':
        temp+=IN[i]
        i+=1
        LIST.append(temp)
        temp=''
    i+=1

matrix=[]

for i in range(len(LIST)):
    matrix.append(string_to_list(LIST[i]))



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


#example
# [[0,0,0,0,0],[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,1]]