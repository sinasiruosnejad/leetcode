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

sum_list=[]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i==j:
            sum_list.append(matrix[i][j])
        elif i+j==len(matrix)-1:
            sum_list.append(matrix[i][j])

print(sum(sum_list))