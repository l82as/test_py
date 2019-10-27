k,t=map(int,input().split())
c=t%k
n=t//k
if c==0 and n%2==0:
    print(0)
if c==0 and n%2!=0:
    print(k)
if c!=0 and n%2==0:
    l=c
    print(l)
if c!=0 and n%2==1:
    l=k-c
    print(l)

        
        
