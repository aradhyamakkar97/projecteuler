p=[] # will contain list of primes 

l=[]
b=[]

for i in range(2,10000000):
    l.append(i)
    b.append(True)
    
indx=0
while(len(p)!=10001):
    if b[indx]:
        p.append(l[indx])
        
        permission =True
        natural=1
        while permission:
            if (indx+l[indx]*natural)<(10000000-5):
                b[indx+l[indx]*natural]=False
                natural+=1
            else:
                permission=False
        
    indx+=1

print (p[10000])    
