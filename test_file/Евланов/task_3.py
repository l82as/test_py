a = int(input())
b = int(input())
m=[]
s=0
d=0
for i in range(b):
    c = int(input())
    m.append(c)
for i in range(len(m)):
    if s + m[i]<a:
        s += m[i]
    else:
        d +=m[i]
print(s)
print(d)
