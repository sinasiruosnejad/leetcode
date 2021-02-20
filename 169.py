nin=input()
x=[]
for i in range(len(nin)):
    x.append(int(nin[i]))


list_of_numbers=[]
status='qualified'
majority=0
for i in range(len(x)):
    status='qualified'
    if i==0:
        list_of_numbers.append([])
        list_of_numbers[i].append(x[i])
    else:
        for j in range(len(list_of_numbers)):
            if list_of_numbers[j][0]==x[i]:
                list_of_numbers[j].append(x[i])
                break
        for j in range(len(list_of_numbers)):
            for k in range(len(list_of_numbers)):
                if list_of_numbers[k][0]==x[i]:
                    status='not qualified'
            if status=='qualified':
                list_of_numbers.append([])
                list_of_numbers[len(list_of_numbers)-1].append(x[i])
                break


for i in range(len(list_of_numbers)):
    
    if len(list_of_numbers[i])>majority:
        majority=len(list_of_numbers[i])
    

for i in range(len(list_of_numbers)):
    if len(list_of_numbers[i])==majority:
        print(f'majority: {list_of_numbers[i][0]}  times repeated: {majority}')



