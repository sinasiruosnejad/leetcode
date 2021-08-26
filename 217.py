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

nums=string_to_list()

list_of_nums=[]

for i in range(len(nums)):
    status=True
    for j in range(len(list_of_nums)):
        if nums[i]==list_of_nums[j][0]:
            status=False
            list_of_nums[j].append(nums[i])
    if status==True:
        list_of_nums.append([nums[i]])

for i in range(len(list_of_nums)):
    if len(list_of_nums[i])>1:
        print('true')
        exit()
else:
    print('false')