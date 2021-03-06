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
B=string_to_list()
C=string_to_list()
D=string_to_list()
if not(len(A)==len(B) and len(B)==len(C) and len(C)==len(D)):
    print("lists don't have the same length")
    exit
result=0
for i in range(len(A)):
    for j in range(len(B)):
        for k in range(len(C)):
            for l in range(len(D)):
                temp=A[i]+B[j]+C[k]+D[l]
                if temp==0:
                    result+=1
print(result)