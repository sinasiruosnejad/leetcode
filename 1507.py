date=input('please enter date: ')
temp=''
day=0
month=0
year=0
status='day'
t=0
months=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
for i in range(len(date)):
    if status=='day':
        if date[i]=='h':
            status='month'
            temp=''
        elif date[i]!='t':
            temp+=date[i]
        elif date[i]=='t':
            day=int(temp)
    elif status=='month':
        if date[i]!=' ' and t<3:
            temp+=date[i]
            t+=1
        elif t==3:
            for j in range(len(months)):
                if temp==months[j]:
                    month=j+1
                    break
            status='year'
            temp=''
    elif status=='year':
        temp+=date[i]
year=int(temp)

print(f"{year}-{month}-{day}")