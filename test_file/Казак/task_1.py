"""
F=open("task_1_input.txt", "r")
N=open("output.txt", "w")

K, T = map(int, F.readline().split())
"""
K = int(input())
T = int(input())

if (T//K)%2==0:
    x=T%K
elif (T//K)%2!=0:
    x=K-T%K

print(x)
    
"""
N.write(str(x))

F.close()
N.close()
"""
