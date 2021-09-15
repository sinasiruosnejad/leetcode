s_in=input()
s=[]

for i in range(len(s_in)):
    stat=True
    for j in range(len(s)):
        if s_in[i]==s[j][0]:
            s[j].append(s_in[i])
            stat=False
            break
    if stat==True:
        s.append([s_in[i]])

stat=False
i=0
while i<len(s):
    if len(s[i])%2!=0 :
        if  len(s[i])>1:
            s[i].pop(0)
        elif len(s[i])==1 :
            if stat==False:
                stat=True
            elif stat==True:
                s.pop(i)
                i-=1
    i+=1
result=0
for i in range(len(s)):
    result+=len(s[i])

print(result)