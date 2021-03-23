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
result=0
for i in range(len(IN)):
    for j in range(i+1,len(IN)):
        if IN[i]==IN[j]:
            result+=1
print(result)