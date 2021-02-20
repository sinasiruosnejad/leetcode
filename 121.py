def string_to_list():
    x=input()
    result=[]
    i=1
    while x[i]!=']':
        if x[i]!=',':
            j=i
            temp=''
            while x[j]!=',':
                if x[j]==']':
                    break
                temp+=x[j]
                j+=1
                i=j
                result.append(int(temp))
        else:
            i+=1
    return result

prices=string_to_list()

profit=[]
for i in range(len(prices)):
    for j in range(i+1,len(prices)):
        temp=prices[j]-prices[i]
        profit.append(temp)
final_profit=0
for i in range(len(profit)):
    if profit[i]>final_profit:
        final_profit=profit[i]

print(final_profit)