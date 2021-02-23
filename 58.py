x=input()
len_word=0
for i in range(len(x)):
    len_word+=1
    if x[i]==' ':
        len_word=0

print(len_word)