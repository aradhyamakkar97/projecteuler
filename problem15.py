l=[]
for i in range(21):
    l.append([])
    for j in range(21):
        if i==0 and j==0:
            l[i].append(0)
        elif i==0 and j!=0:
            l[i].append(1)
        elif i!=0 and j==0:
            l[i].append(1)
        else:
            l[i].append(l[i-1][j]+l[i][j-1])

print (l[20][20])            
