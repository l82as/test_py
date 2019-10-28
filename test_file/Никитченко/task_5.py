R, G, B = map(int,input().split())
a=abs(R-G)
c=abs(R-B)
d=abs(G-B)
if a<=25 and c<=25 and d<=25:
    print('ALLOWED')
else:
    print('FORBIDDEN')
