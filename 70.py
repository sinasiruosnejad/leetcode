steps=int(input())

def possibilities(steps):
    if steps==0 or steps==1:
        return 1
    else:
        possible_ways=possibilities(steps-1)+possibilities(steps-2)
        return possible_ways


print(possibilities(steps))