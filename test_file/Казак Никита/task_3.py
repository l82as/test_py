"""
def check(n):
    if n%3==0:
        return True
    else:
        return False

n=int(input("n = "))            #Число

t=len(str(n))-1                 #Разрядность n
arr=[]
for i in range(t, 0, -1):
    #for k in range(n, 10**(t+1), 10**i):
    #   if  check()
    print(t)
    for k in range(10**i, 10**(t+1), 10**t):
        if check(n+k)==True and n+k<10**(t+1):
            print("k = ", k)
            print("n+k = ", n+k)
            arr.append(n+k)

print("arr = ", arr)
        
"""
n=int(input())

t=len(str(n))-1 				#Разряд числа -1
arr=[]
for i in range(t, 0, -1):
	for k in range(10**i, 10**(i+1), 10**i):
		if (n+k)%3==0 and n+k<10**(i+1):
			arr.append(n+k)
m=arr[0]
for i in range(len(arr)):
	if m<arr[i]:
		m=arr[i]

print(m)
