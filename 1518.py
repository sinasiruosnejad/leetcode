numBottles=int(input('pleas enter the number of full buttles: '))
numExchange=int(input('pleas enter number of empty bottels to exchange with full bottels: '))

fullbottels=numBottles
result=0
while numBottles>=numExchange or fullbottels>0:
    result+=fullbottels
    fullbottels=numBottles//numExchange
    numBottles%=numExchange
    numBottles+=fullbottels

print(result)