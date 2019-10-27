"""F=open("task_2_input.txt", "r")
N=open("output.txt", "w")

P, S = map(int, F.readline().split())
"""
P, S = map(int, input("P, S = ").split())

x=(P-(P**2-4*S)**0.5)/2
y=(P+(P**2-4*S)**0.5)/2

print("x = ", x)
print("y = ", y)

"""
N.write(str(x))

F.close()
N.close()
"""
