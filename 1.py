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


numbers=[]
string_to_list('numbers: ',numbers)
target=int(input('target: '))

for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        temp=numbers[i]+numbers[j]
        if target==temp:
            print(f'[{i},{j}]')
            exit()