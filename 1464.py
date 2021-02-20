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

num=string_to_list()


results=[]
for i in range(len(num)):
    for j in range(i+1,len(num)):
        temp=(num[i]-1)*(num[j]-1)
        results.append(temp)

final_result=results[0]
for i in range(len(results)):
    if final_result<results[i]:
        final_result=results[i]

print(final_result)