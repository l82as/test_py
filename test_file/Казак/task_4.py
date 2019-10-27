S=int(input("S = "))
N=int(input("N = "))

m1=0                        #Масса вещей в рюкзаке
m2=0                        #Масса вещей в чемодане
for i in range(1, N+1):
    string="m"+str(i)+" = "
    m=int(input(string))    #Масса вещи
    if m<=S and m1+m<S:
        m1+=m
    elif m>S or m1+m>S:
        m2+=m

print("m в рюкзаке = ", m1)
print("m в чемодане = ", m2)
