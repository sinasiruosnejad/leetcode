def string_to_list(string):
    x=input(string)
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

nums=string_to_list("please enter list of numbers: ")

target=int(input('please enter the target: '))

for i in range(len(nums)):
    if nums[i]<=target:
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                result=[i+1,j+1]
                break

print(result)