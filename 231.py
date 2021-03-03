x=int(input())
test=0
i=-1
while x>test:
    i+=1
    test=2**i

if x==test:
    print('true')
else:
    print('false')
