n=int(input())

divisors=[2,3,5]
i=0
while n!=1:
    if (n%divisors[i])==0:
        n=n/divisors[i]
    else:
        i+=1
    if i>2:
        print('false')
        exit()
print('true')