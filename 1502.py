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
arr.sort()
difference=arr[1]-arr[0]
result='true'
for i in range(1,len(arr)):
    if arr[i]-arr[i-1]!=difference:
        result='false'

print(result)