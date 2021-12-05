f=open('input.txt','r').readlines()

hor = 0
ver = 0
for i in f:
    a,b = i.split()
    if a=='forward':
        hor += int(b)
    if a=='down':
        ver += int(b)
    if a=='up':
        ver -= int(b)

print(hor*ver)
