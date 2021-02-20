a=input('\nplease enter a roman numeral: ')
result=0
x=[]
for i in range(len(a)):
    x.append(a[i])


for i in range(len(x)):
    if len(x)>0:
        for j in range(1):
            if len(x)>=2:
                if x[j]=='I' and x[j+1]=='V':
                    result+=4
                    x.pop(j)
                    x.pop(j)
                    break
                elif x[j]=='I' and x[j+1]=='X':
                    result+=9
                    x.pop(j)
                    x.pop(j)
                    break
                elif x[j]=='X' and x[j+1]=='L':
                    result+=40
                    x.pop(j)
                    x.pop(j)
                    break
                elif x[j]=='X' and x[j+1]=='C':
                    result+=90
                    x.pop(j)
                    x.pop(j)
                    break
                elif x[j]=='C' and x[j+1]=='D':
                    result+=400
                    x.pop(j)
                    x.pop(j)
                    break
                if x[j]=='C' and x[j+1]=='M':
                    result+=900
                    x.pop(j)
                    x.pop(j)
                    break
                elif x[j]=='I':
                    result+=1
                    x.pop(j)
                    break
                elif x[j]=='V':
                    result+=5
                    x.pop(j)
                    break
                elif x[j]=='X':
                    result+=10
                    x.pop(j)
                    break
                elif x[j]=='L':
                    result+=50
                    x.pop(j)
                    break
                elif x[j]=='C':
                    result+=100
                    x.pop(j)
                    break
                elif x[j]=='D':
                    result+=500
                    x.pop(j)
                    break
                elif x[j]=='M':
                    result+=1000
                    x.pop(j)
                    break
            else:
                if x[j]=='I':
                    result+=1
                    x.pop(j)
                    break
                elif x[j]=='V':
                    result+=5
                    x.pop(j)
                    break
                elif x[j]=='X':
                    result+=10
                    x.pop(j)
                    break
                elif x[j]=='L':
                    result+=50
                    x.pop(j)
                    break
                elif x[j]=='C':
                    result+=100
                    x.pop(j)
                    break
                elif x[j]=='D':
                    result+=500
                    x.pop(j)
                    break
                elif x[j]=='M':
                    result+=1000
                    x.pop(j)
                    break
        

print(f'it equals to: {result}')