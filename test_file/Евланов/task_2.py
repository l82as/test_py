a, b = map(int, input().split())

c=b%a
x=b//a
if c==0 and x%2==0:
    print(0)
if c==0 and x%2!=0:
    print(k)
if c!=0 and x%2==0:
    m=c
    print(l)
if c!=0 and x%2==1:
    m=a-c
    print(m)
