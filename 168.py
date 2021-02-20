x=int(input('\n'))

ascii_num=64
ascii_number=64
if x>26:
    ascii_number+=(x//26)
    if x%26==0:
        ascii_num+=26
    else:
        ascii_num+=(x%26)
    a=chr(ascii_number)
    b=chr(ascii_num)
    print(f'{a}{b}')
else:
    if x==26:
        ascii_num+=x
    else:
        ascii_num+=(x%26)
    b=chr(ascii_num)
    print(f'{b}')

