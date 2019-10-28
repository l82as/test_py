S=int(input())
N=int(input())
R=0
B=0
for i in range(n):
    i=int(input())
    if R+i<s:
        R+=i
    else:
        B+=i
print(R)
print(B)
