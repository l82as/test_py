S=int(input())
N=int(input())

m1=0                        #Масса вещей в рюкзаке
m2=0                        #Масса вещей в чемодане
for i in range(1, N+1):
    
    m=int(input())    #Масса вещи
    if m<=S and m1+m<S:
        m1+=m
    elif m>S or m1+m>S:
        m2+=m

print( m1)
print( m2)
