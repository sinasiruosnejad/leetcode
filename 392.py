s_in=input()
t_in=input()
s=[]
t=[]
for i in range(len(s_in)):
    s.append(s_in[i])
for i in range(len(t_in)):
    t.append(t_in[i])

status=0
for i in range(len(t)):
    for  j in range(1):
        if t[i]==s[j]:
            status+=1
            s.pop(j)
            break

if status==len(s_in):
    print('true')
else:
    print('false')