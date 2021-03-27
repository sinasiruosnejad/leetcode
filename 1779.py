import math
def string_to_list(value):
    x=value
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

tt=input('please enter the x and y value: ')
xy=string_to_list(tt)
t=input('please enter the list of points: ')
temp=''
other_temp=[]
for i in range(1,len(t)-1):
    if t[i]!=',':
        temp+=t[i]
    else:
        other_temp.append(temp)
        temp=''

points=[]

for i in range(len(other_temp)):
    temp=string_to_list(other_temp[i])


qualified=[]
distance=[]
qualify=[]
finall_qualification=[]
for i in range(len(points)):
    if xy[0]==points[i][0] or xy[1]==points[i][1]:
        qualified.append([points[i],i])

for i in range(len(qualified)):
    temp=math.sqrt(((xy[0]-qualified[i][0][0])**2)+((xy[1]-qualified[i][0][1])**2))
    distance.append(temp)

for i in range(len(distance)):
    if i==0:
        temp=distance[i]
        temp_i=i
    elif temp<distance[i]:
        temp=distance[i]
        temp_i=i
        qualify.pop(0)
        qualify.append(temp_i)
    elif temp==distance[i]:
        qualify.append(i)

for i in range(len(qualify)):
    finall_qualification.append(qualified[i][1])

for i in range(len(finall_qualification)):
    if i==0:
        result=finall_qualification[i]
    elif temp>finall_qualification[i]:
        result=finall_qualification[i]

print(result)