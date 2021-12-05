f=open('input.txt','r').readlines()

hor = 0
ver = 0
aim=0
for i in f:
    a,b = i.split()
    if a=='forward':
        hor += int(b)
        ver += aim*int(b)
    if a=='down':
        aim += int(b)
    if a=='up':
        aim -= int(b)

print(hor*ver)
