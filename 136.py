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

nums=string_to_list()


for i in range(len(nums)):
    status=True
    for j in range(len(nums)):
        if i!=j and nums[i]==nums[j]:
            status=False
    if status:
        result=nums[i]
        break

print(result)