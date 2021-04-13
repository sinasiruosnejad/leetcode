string1=input()
string2=input()

def string_to_list(s):
    l=[]
    for i in range(len(s)):
        l.append(s[i])
    return l

list1=string_to_list(string1)
list2=string_to_list(string2)
if list1==list2:
    print('true')
    exit()
i=0
while i<len(list1):
    j=0
    while j<len(list2) and i<len(list1):
        if list1[i]==list2[j]:
            list1.pop(i)
            list2.pop(j)
            i-=1
            break
        else:
            j+=1
    i+=1

if not(len(list1)==0 and len(list2)==0):
    print('false')
    exit()

list1=string_to_list(string1)
list2=string_to_list(string2)
attempts=0
i=0
while i <len(list1) and i <len(list2):
    if list1[i]!=list2[i]:
        j=i
        while j<len(list1):
            if list1[i]==list2[j]:
                temp=list2[i]
                list2[i]=list2[j]
                list2[j]=temp
                attempts+=1
                break
            j+=1
    i+=1

if attempts<=2 and list1==list2:
    print('true')
else:
    print('false')