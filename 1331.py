def string_to_list(string):
    x=input(str(string))
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

IN=string_to_list('please enter the array: ')
examing=[]
orders=[]
result=[]
for i in range(len(IN)):
    examing.append([IN[i],i])

for i in range(len(examing)):
    for j in range(len(examing)-1):
        if examing[j][0]>examing[j+1][0]:
            temp=examing[j]
            examing[j]=examing[j+1]
            examing[j+1]=temp

status='ok'
x=1
for i in range(len(examing)):
    if status=='not ok':
        x-=1
        status='ok'    
    if examing[i][0]==examing[i-1][0] and i>0:
        orders.append([orders[-1:][0][0],examing[i][1]])
        status='not ok'
    else:
        orders.append([i+x,examing[i][1]])


for i in range(len(orders)):
    for j in range(len(orders)):
        if orders[j][1]==i:
            result.append(orders[j][0])
            break

print(result)
