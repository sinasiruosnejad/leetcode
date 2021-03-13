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
status='even'
while len(IN)>0:
    if status=='even':
        for j in range(len(IN)):
            if IN[j]%2==0:
                result.append(IN[j])
                IN.pop(j)
                break
        status='odd'
    elif status=='odd':
        for j in range(len(IN)):
            if IN[j]%2==1:
                result.append(IN[j])
                IN.pop(j)
                break
        status='even'

print(result)