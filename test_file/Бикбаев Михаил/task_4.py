s=int(input())
n=int(input())
r=0
h=0
for i in range(n):
    a=int(input())
    if (s-r)>=a:
        r+=a
    else:
        h+=a
print(r,h)
