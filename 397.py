n=int(input())

if n<0:
    n*=-1
    
def operation(n,x):
    counter=0
    while n!=1:
        if n%2==0:
            n/=2
            counter+=1
        else:
            n+=x
            counter+=1
    return counter

result1=operation(n,1)
result2=operation(n,-1)

if result1>=result2:
    print(result2)
else:
    print(result1)