K=int(input())
T=int(input())
if (T//K)%2==0:
    B=T%K
else:
    B=K-T%K
print(B)
