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
    
arr=string_to_list()

arr=sorted(arr)
result=''
for i in range(len(arr)):
    if result=='true':
        break
    for j in range(i+1,len(arr)):
        if arr[i]*2==arr[j]:
            result='true'
            break
else:
    result='false'

print(result)