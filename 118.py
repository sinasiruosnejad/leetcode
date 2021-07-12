num_rows=int(input())

def function(list_num):
    result=[1]
    for i in range(len(list_num)-1):
        temp=list_num[i]+list_num[i+1]
        result.append(temp)
    result.append(1)
    return result
    
result=[[1]]
for i in range(num_rows-1):
    temp=function(result[-1])
    result.append(temp)

print(result)