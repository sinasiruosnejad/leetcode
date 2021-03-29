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

frequency=[]
qualified=[]
for i in range(len(num)):
    status='not frequent'
    for j in range(len(frequency)):
        if frequency[j][0]==num[i]:
            frequency[j].append(num[i])
            status='frequent'
    if status=='not frequent':
        frequency.append([num[i]])

for i in range(len(frequency)):
    if len(frequency[i])==frequency[i][0]:
        qualified.append(frequency[i][0])

result=-1
for i in range(len(qualified)):
    if i==0:
        result=qualified[i]
    elif result<qualified[i]:
        result=qualified[i]

print(result)