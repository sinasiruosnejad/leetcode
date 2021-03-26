words_in=input("please enter words: ")
l=0
words=[]
temp=''
while l<len(words_in):
    if words_in[l]!= ',' and words_in[l]!= '[' and words_in[l]!= '"' and words_in[l]!= ']':
        temp+=words_in[l]
    else:
        if temp!='':
            words.append(temp)
            temp=''
    l+=1



chars_in=input("please enter characters: ")
def lis(IN):
    temp=[]
    for i in range(len(IN)):
        temp.append(IN[i])
    return temp

result=0
for i in range(len(words)):
    temp_chars=lis(chars_in)
    temp_word=lis(words[i])
    j=0
    len_temp=len(temp_word)
    while len(temp_word)>j:
        k=0
        while k<len(temp_chars) and len(temp_word)>0 and len(temp_word)>j:
            if temp_word[j]==temp_chars[k]:
                temp_chars.pop(k)
                temp_word.pop(j)
                k=0
            else:
                k+=1
        j+=1
    if len(temp_word)==0:
        result+=len_temp

print(result)

            