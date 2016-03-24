p=[] # will contain list of primes 

l=[]
b=[]

for i in range(2,2000000):
    l.append(i)
    b.append(True)
    
indx=0
while(indx!=(2000000-2)):
    if b[indx]:
        p.append(l[indx])
        
        permission =True
        natural=1
        while permission:
            if (indx+l[indx]*natural)<(2000000-2):
                b[indx+l[indx]*natural]=False
                natural+=1
            else:
                permission=False
        
    indx+=1
summ=0
for s in p:
    summ+=s
    
print (summ)    
