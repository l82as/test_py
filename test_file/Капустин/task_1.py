K=int(input())
T=int(input())
f=0
while T>0:
    if f==0:
        while f<K and T>0:
            f+=1
            T-=1
    if f==K:
        while f>0 and T>0:
            f-=1
            T-=1
print (f)
