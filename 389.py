s=list(input())
t=list(input())


j=0
while j<len(t) and len(s)!=0:
    if s[0]==t[j]:
        s.pop(0)
        t.pop(j)
    else:
        j+=1

print(t[0])