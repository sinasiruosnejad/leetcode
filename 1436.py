IN=input('please enter the paths: ')

paths=[]
temp_temp=[]
temp=''
for i in range(len(IN)):
    if IN[i]!='[' and IN[i]!='"' and IN[i]!=',' and IN[i]!=']':
        temp+=IN[i]
    elif IN[i]==',' and IN[i-1]!='[' or i==len(IN)-2:
        temp_temp.append(temp)
        temp=''
    else:
        if (len(temp_temp))==2:
            paths.append(temp_temp)
            temp_temp=[]

if len(paths)==1:
    result=paths[0][1]
else:
    for i in range(1,len(paths)):
        for j in range(i):
            if paths[i][0]==paths[j][1]:
                result=paths[i][1]

print(result)