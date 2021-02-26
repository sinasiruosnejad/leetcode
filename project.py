n=input()
IN=[]
for i in range(len(n)):
    IN.append(int(n[i]))

x_status='left'
y_status='left'
z_status='left'
result=''

for i in range(len(IN)):
    if IN[i]==2:
        if x_status=='left':
            IN[i]=1
            x_status='right'
        elif x_status=='right':
            IN[i]=3
            x_status='left'
    if IN[i]==1:
        if y_status=='left':
            result+='A'
            y_status='right'
        elif y_status=='right':
            result+='B'
            y_status='left'
    elif IN[i]==3:
        if z_status=='left':
            result+='B'
            z_status='right'
        elif z_status=='right':
            result+='C'
            z_status='left'
    

print(result)