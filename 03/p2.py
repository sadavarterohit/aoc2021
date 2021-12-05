def bin_to_dec(a):
    ret = 0
    pow = 0
    
    for i in a[::-1]:
        
        
        ret += int(i)*2**pow
        pow+=1
    
    return ret

f=open('input.txt','r').read().split('\n')

g= f.copy()

l = len(f[0])

j=0

while(len(f)>1):
    new_f = []
    zero = 0
    one = 0
    for i in f:
        if(i[j] =='0'):
            zero+=1
        else:
            one+=1
    #print(one, zero)
    if(one >= zero):
        for i in f:
            if(i[j] == '1'):
                
                new_f.append(i)
                

    else:
        for i in f:
            if(i[j]=='0'):
                new_f.append(i)
    f= new_f.copy()
    
    j+=1

j=0
while(len(g)>1):
    new_g = []
    zero = 0
    one = 0
    for i in g:
        if(i[j] =='0'):
            zero+=1
        else:
            one+=1
    #print(one, zero)
    if(one < zero):
        for i in g:
            if(i[j] == '1'):
                
                new_g.append(i)
                

    else:
        for i in g:
            if(i[j]=='0'):
                new_g.append(i)
    g= new_g.copy()
    
    j+=1
#print(f,g)
print(bin_to_dec(f[0]) * bin_to_dec(g[0]))