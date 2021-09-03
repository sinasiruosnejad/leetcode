pattern=input('enter pattern: ')
string_input=input('enter string: ')

pattern_code=[]
string=[]
string_code=[]

code=0
for i in range(len(pattern)):
    for j in range(len(pattern_code)):
        if pattern_code[j][1]==pattern[i]:
            pattern_code.append([pattern_code[j][0],pattern[i]])
            break
    else:
        pattern_code.append([code,pattern[i]])
        code+=1

temp=''
string_input+=' '
for i in range(len(string_input)):
    if string_input[i]!=' ':
        temp+=string_input[i]
    else:
        string.append(temp)
        temp=''

code=0
for i in range(len(string)):
    for j in range(len(string_code)):
        if string_code[j][1]==string[i]:
            string_code.append([string_code[j][0],string[i]])
            break
    else:
        string_code.append([code,string[i]])
        code+=1

print(pattern_code)
print(string_code)

for i in range(len(pattern_code)):
    if pattern_code[i][0]!=string_code[i][0]:
        print('false')
        exit()
else:
    print('true')