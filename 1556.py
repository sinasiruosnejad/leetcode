IN=input('\n')
x=''
result=''
if len(IN)%3!=0:
    for  i in range(len(IN)%3):
        result+=IN[i]

    for i in range(len(IN)%3,len(IN)):
        x+=IN[i]

    for i in range(len(x)):
        if i%3==0:
            result+='.'
        result+=x[i]

else:
    x=IN
    for i in range(len(x)):
        if i%3==0 and i!=0:
            result+='.'
        result+=x[i]


print(result)