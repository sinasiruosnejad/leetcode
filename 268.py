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

nums.sort()

nums_alt=[]
for i in range(len(nums)+1):
    nums_alt.append(i)

i=0
while len(nums)!=0:
    if nums[i]==nums_alt[i]:
        nums.pop(i)
        nums_alt.pop(i)
    else:
        nums_alt.append(nums_alt[i])
        nums_alt.pop(i)


print(nums_alt[0])