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

lis=string_to_list()
k=int(input())

if k>len(lis):
    print(f'{k} is bigger than length of the list')
    exit

result=[]
for i in range(len(lis)-k+1):
    temp=0
    for j in range(i,i+k):
        temp+=lis[j]
    result.append(temp)

for i in range(len(result)):
    if i==0:
        t=result[i]
    elif t<result[i]:
        t=result[i]

print(t/k)