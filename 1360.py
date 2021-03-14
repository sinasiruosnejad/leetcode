print("date format YYYY-MM-DD")
date1=input("pleas enter the starting date: ")
date2=input("pleas enter the finish date: ")


def IN(date):
    status='year'
    temp=''
    D={'year':0,'month':0,'day':0}
    date+='-'
    for i in range(len(date)):
        if date[i]!='-':
            temp+=date[i]
        elif date[i]=='-':
            if status=='year':
                D.update({'year':int(temp)})
                temp=''
                status='month'
            elif status=='month':
                 D.update({'month':int(temp)})
                 temp=''
                 status='day'
            elif status=='day':
                D.update({'day':int(temp)})
    return D

D1=IN(date1)
D2=IN(date2)
month=[31,28,31,30,31,30,31,31,30,31,30,31]
result=0
leap=0
while True:
    if D1['year']==D2['year'] and D1['month']==D2['month'] and D1['day']==D2['day']:
        break
    if result==0:
        if D1['year']%4!=0:
            leap+=0
        elif D1['year']%100!=0:
            leap+=1
        elif D1['year']%400!=0:
            leap+=0
        else:
            leap+=1

    t=D1['month']-1
    goal=month[t]
    if D1['day']==goal:
        temp=D1['month']
        temp+=1
        D1.update({'month':temp})
        D1.update({'day':0})
    if D1['month']>12:
        temp=D1['year']
        temp+=1
        D1.update({'year':temp})
        D1.update({'month':1})
        if D1['year']%4!=0:
            leap+=0
        elif D1['year']%100!=0:
            leap+=1
        elif D1['year']%400!=0:
            leap+=0
        else:
            leap+=1
    d=D1['day']
    d+=1
    D1.update({'day':d})
    result+=1
    

print(result+leap)
        



