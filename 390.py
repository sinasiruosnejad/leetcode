arr=[]
n=int(input())

for i in range(1,n+1):
    arr.append(i)

steps=-1
while len(arr)!=1:
    steps*=-1
    if steps==1:
        arr.sort()
    elif steps==-1:
        arr.sort(reverse=True)

    for i in range(len(arr)):
        if i>=len(arr):
            break
        arr.pop(i)

print(arr[0])