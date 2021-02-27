def string_to_list():
    x=input()
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



IN=string_to_list()
result=[]
for i in range(len(IN)):
    for j in range(i+1,len(IN)):
        for k in range(j+1,len(IN)):
            temp=IN[i]+IN[j]+IN[k]
            list_temp=[]
            list_temp.append(IN[i])
            list_temp.append(IN[j])
            list_temp.append(IN[k])
            if temp==0:
                result.append(list_temp)
                for l in range(len(result)-1):
                    temp1=sorted(result[l])
                    temp2=sorted(list_temp)
                    if temp1==temp2:
                        result.pop(len(result)-1)
print(result)