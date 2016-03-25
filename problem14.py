maxx=0
def noe(num):
    ans=0
    while(num!=1):
        if num%2==0:
            num=num/2
            ans+=1
        else:
            num=num*3+1
            ans+=1
    return ans+1            
for i in range(2,1000000):
    if noe(i)>maxx:
        maxx=noe(i)
        note_i=i
    
print(note_i)
print (maxx)
