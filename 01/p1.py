f=open('input.txt','r').read()
a=list(map(int,f.split()) )
count =0 
for i in range(len(a)-1):
    if(a[i+1]>a[i]):
        count +=1

print(count)
    