days=int(input())
saved=0
monday=0
other_days=0
for i in range(days):
    if i==0 or i%7==0:
        monday+=1
        saved+=monday
        other_days=monday
    else:
        saved+=other_days
    other_days+=1

print(saved)