num=input()

while True:
    if int(num)<10:
        break
    digits=[]
    temp=0
    for i in range(len(num)):
        digits.append(int(num[i]))
    for j in range(len(digits)):
        temp+=digits[j]
    num=str(temp)

print(num)