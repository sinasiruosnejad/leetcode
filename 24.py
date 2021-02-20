a=input()
x=[]
for i in range(len(a)):
    if i%2==1:
        temp=int(a[i])
        x.append(temp)


L=len(x)-1
LEN=len(x)
status='zoj'

if LEN%2==1:
    LEN-=1
    status='fard'
last_int=0

for i in range(0,LEN,2):
    if len(x)%2==1:
        last_int=x[-1:]
        x.pop(L)
    temp=x[i]
    x[i]=x[i+1]
    x[i+1]=temp

if status=='fard':
    x.append(last_int)

print(x)

    