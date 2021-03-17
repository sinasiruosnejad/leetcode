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


candidates=[]
status='first'

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if j==0:
            temp=matrix[i][j]
            tempJ=j
        elif temp>matrix[i][j]:
            temp=matrix[i][j]
            tempJ=j
    if status=='first':
        candidates.append([tempJ,temp])
        status='not first'
    else:
        status='do'
        for k in range(len(candidates)):
            if candidates[k][0]==tempJ :
                status="don't"
                if candidates[k][1]<temp:
                    candidates[k][1]=temp
        if status=='do':
            candidates.append([tempJ,temp])

qualified=[]

for i in range(len(candidates)):
    x=candidates[i][0]
    temp=candidates[i][1]
    status='qualified'
    for j in range(len(matrix)):
        if temp<matrix[j][x]:
            status='not qualified'
            break
    if status=='qualified':
        qualified.append(temp)

print(qualified)



# examples

# [3,7,8]
# [9,11,13]
# [15,16,17]

# [1,10,4,2]
# [9,3,8,7]
# [15,16,17,12]