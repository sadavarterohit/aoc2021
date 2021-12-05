def bin_to_dec(a):
    ret = 0
    pow = 0

    for i in a[::-1]:
        ret += i*2**pow
        pow+=1
    
    return ret



f=open('input.txt','r').readlines()

l = len(f[0]) -1

eps = [0]*l

for j in range(l):
    zero = 0
    one = 0
    for i in f:
        if(i[j] =='0'):
            zero+=1
        else:
            one+=1

    if(one > zero):
        eps[j] = 1


gr = [0]*l

for j in range(l):
    zero = 0
    one = 0
    for i in f:
        if(i[j] =='0'):
            zero+=1
        else:
            one+=1

    if(one < zero):
        gr[j] = 1



print(bin_to_dec(eps)* bin_to_dec(gr))




