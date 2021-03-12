stringA=input('pleas enter a string: ')
stringB=input('pleas enter a string: ')
S_A=[]
S_B=[]
for i in range(len(stringA)):
    S_A.append(stringA[i])

for i in range(len(stringB)):
    S_B.append(stringB[i])
i=0
while len(S_A)>0 and len(S_B)>0 and i<len(S_A):
    j=0
    while len(S_B)>0 and len(S_A)>0 and j<len(S_B) and i<len(S_A):
        if S_A[i]==S_B[j]:
            S_A.pop(i)
            S_B.pop(j)
            j=0
        else:
            j+=1
    i+=1

if len(S_A)>0 or len(S_B)>0:
    print('false')
else:
    print('true')
