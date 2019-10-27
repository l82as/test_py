K=int(input())
T=int(input())
x=0
while T>0:
    if x==0:
        while x<K and T>0:
            x+=1
            T-=1
    if x==K:
        while x>0 and T>0:
            x-=1
            T-=1
print(x)
