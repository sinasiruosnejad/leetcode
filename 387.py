s=input('[lease enter an string: ')

repeats=[]

for i in range(len(s)):
    status='ok'
    for j in range(len(repeats)):
        if repeats[j][0]==s[i]:
            repeats[j][1]+=1
            status='not ok'
    if status=='ok':
        repeats.append([s[i],1,i])
i=0
while i<len(repeats):
    if repeats[i][1]!=1:
        repeats.pop(i)
        i-=1
    i+=1

if len(repeats)>0:
    print(repeats[0][2])
else:
    print(-1)