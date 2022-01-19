#count all 5 in between 0 to 100 in mathematical way
a=1
for i in range(0,100):
    if i%10==5 or round(i/10)==5:
        a=a+1

print(a)
    
