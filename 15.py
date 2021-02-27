IN=[-1,0,1,2,-1,-4]
result=[]
for i in range(len(IN)):
    for j in range(len(IN)):
        for k in range(len(IN)):
            temp=IN[i]+IN[j]+IN[k]
            list_temp=[]
            list_temp.append(IN[i])
            list_temp.append(IN[j])
            list_temp.append(IN[k])
            if temp==0:
                for l in range(len(result)+1):
                    if l==0:
                        result.append(list_temp)
                    temp1=sorted(result[l])
                    temp2=sorted(list_temp)
                    if temp1!=temp2:
                        result.append(list_temp)


print(result)