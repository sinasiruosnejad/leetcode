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

slope=[]
for i in range(1,len(matrix)):
    tsx=matrix[i][0]-matrix[i-1][0]
    tsy=matrix[i][1]-matrix[i-1][1]
    if i==1:
        slope.append(tsx)
        slope.append(tsy)
    elif slope[0]!=tsx or slope[1]!=tsy:
        print('false')
        break
else:
    print('true')