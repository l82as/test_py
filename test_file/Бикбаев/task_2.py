s,p=map(int,input().split())
c=0
k=0
for i in range(1,s+1):
    k+=1
    c=s-k
    if (k*c)==p:
        break
print(k,c)
