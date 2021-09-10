s_input=input()
k=int(input())
result=0
s=[]
for i in range(len(s_input)):
    status=True
    for j in range(len(s)):
        if s_input[i]==s[j][0]:
            s[j].append(s_input[i])
            status=False
            break
    if status==True:
        s.append([s_input[i]])

for i in range(len(s)):
    if len(s[i])>=k:
        result+=len(s[i])

print(result)