import math
i=1

def nod(num):
    ans=0
    for j in range(1,int(math.sqrt(num))):
        if (num%j)==0:
            ans+=1
    if num%math.sqrt(num)!=0:
        return 2*ans
    else:
        return 2*ans-1
while(True):
    n=(i*(i+1))//2
    if nod(n)>500:
        break
    i+=1


print(n)    
    
