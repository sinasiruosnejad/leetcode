num=int(input())
i=0
while num>0:
    if num%2==0:
        num/=2
    else:
        num-=1
    i+=1
print(i)