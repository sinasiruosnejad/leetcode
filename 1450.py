def string_to_list(string,array):
    x=input(string)
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
            array.append(int(temp))
        else:
            i+=1

start_time=[]
end_time=[]
query_time=0
students_count=0
string_to_list('start time : ',start_time)
string_to_list('end time : ',end_time)
query_time=int(input('query time : '))


if not(1<=len(start_time)<=100):
    print('start time list out of range')
    exit()
elif not(1<=len(end_time)<=100):
    print('end time list out of range')
    exit()
elif len(start_time)!=len(end_time):
    print('length of lists start and end are not the same')
    exit()
elif not(1<=query_time<=1000):
    print('query time out of range')
    exit()

for i in range(len(start_time)):
    if not(1<=start_time[i]<=1000):
        print(f'start time [{i}] out of range')
        exit()
    elif not(1<=end_time[i]<=1000):
        print(f'end time [{i}] out of range')
        exit()
    if start_time[i]<=end_time[i]:
        temp=end_time[i]-start_time[i]
    if temp>=query_time:
        students_count+=1

print(students_count)