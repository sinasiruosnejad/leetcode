x=int(input("\nplease enter an integer "))



number=[]

x_sign="positive"

if x<0:
    x*=-1
    x_sign="negative"


while x!=0:
    temp=x%10
    number.append(temp)
    x=x//10
    

for i in range(len(number)-1,-1,-1):
    if number[i]>0:
        break
    if number[i]==0:
        number.pop(i)


for i in range(len(number)):
    for j in range(1):
        
        if number[j]>0:
            break
        if number[j]==0:
            number.pop(j)





number_replace=[] 
result=0
for i in range(len(number)-1,-1,-1):
    number_replace.append(number[i])

for i in range(len(number_replace)):
    result+=number_replace[i]*(10**i)

if x_sign=="negative":
    result*=-1

r=2**31
if result>r-1 or result<-r:
    result=0


print(result)