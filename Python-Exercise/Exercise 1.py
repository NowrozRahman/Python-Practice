list = [1,4,2,6,'A','N','C']




listtostr = ''.join(map(str,list))


print(listtostr)

n= []
a= []

for i in listtostr:
    if i.isdigit():
        n.append(int(i))
    if i.isalpha():
        a.append(i)

n.sort()
a.sort()

list3 = n+a

print(list3)

















