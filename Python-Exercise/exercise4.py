#count all 5 in between 1 to 100 in string way
a=0
for i in range(0,100):

    z=str(i)
    #0-9
    if int(z)<10 and z[0]=="5":
        a=a+1
    
    #10-100
    if int(z)>10 and z[0]=="5":
        a=a+1
    
    if int(z)>10 and z[1]=="5":
        a=a+1

print(a)
