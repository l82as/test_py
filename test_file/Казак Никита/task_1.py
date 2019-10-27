"""
F=open("task_1_input.txt", "r")
N=open("output.txt", "w")

K, T = map(int, F.readline().split())
"""
K, T = map(int, input("K, T = ").split())

if (T//K)%2==0:
    x=T%K
elif (T//K)%2!=0:
    x=K-T%K

print("x = ", x)
    
"""
N.write(str(x))

F.close()
N.close()
"""
