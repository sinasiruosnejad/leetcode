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

def odd_number(num):
    status='odd'
    if num==1:
        status=''
    for i in range(2,num//2+1):
        if num%i==0:
            status='even'
            break
    return status

num=string_to_list()
result=[]
for i in range(len(num)):
    if odd_number(num[i])=='odd':
        result.append(num[i])

if len(result)>=3:
    print('true')
else:
    print('false')