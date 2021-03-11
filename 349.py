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


arr1=string_to_list()
arr2=string_to_list()
result=[]
for i in range(len(arr1)):
    for j in range(len(arr2)):
        status='ok'
        if arr1[i]==arr2[j]:
            for k in range(len(result)):
                if result[k]==arr2[j]:
                    status='not ok'
            if status=='ok':
                result.append(arr2[j])

print(result)