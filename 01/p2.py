f=open('input.txt','r').read()
a=list(map(int,f.split()) )
count =0
prevsum=0
sum_now=0
for i in range(len(a)-3):
    prev_sum = sum_now
    sum_now = a[i] + a[i+1] + a[i+2]

    if(sum_now > prev_sum):
        count +=1
    

print(count)
    