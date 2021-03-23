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

def perimeter(triangle):
    if len(triangle)>3:
        exit()
    biggestLength=0
    biggestLength_i=0
    otherTwo=[]
    for i in range(len(triangle)):
        if biggestLength<triangle[i]:
            biggestLength=triangle[i]
            biggestLength_i=i

    for i in range(len(triangle)):
        if i!=biggestLength_i:
            otherTwo.append(triangle[i])
    result=0
    if  biggestLength<otherTwo[0]+otherTwo[1]:
        for i in range(len(triangle)):
            result+=triangle[i]
    return result


lengths=string_to_list()

triangles=[]
status='ok'
for i in range(len(lengths)):
    for j in range(i+1,len(lengths)):
        for k in range(j+1,len(lengths)):
            temp=[]
            temp.append(lengths[i])
            temp.append(lengths[j])
            temp.append(lengths[k])
            temp.sort()
            for l in range(len(triangles)):
                if temp == triangles[l]:
                    status='not ok'
            if status=="ok":
                triangles.append(temp)

results=[]
for i in range(len(triangles)):
    results.append(perimeter(triangles[i]))

for i in range(len(results)):
    if i==0:
        finall=results[i]
    elif finall<results[i]:
        finall=results[i]

print(finall)