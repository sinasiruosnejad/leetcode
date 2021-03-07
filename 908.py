import random
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

A=string_to_list()
K=int(input())

for i in range(len(A)):
    temp=random.randint(-K,K)
    A[i]+=temp

print(A)