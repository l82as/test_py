"""F=open("task_2_input.txt", "r")
N=open("output.txt", "w")

P, S = map(int, F.readline().split())
"""
P, S = map(int, input().split())

x=round((P-(P**2-4*S)**0.5)/2)
y=round((P+(P**2-4*S)**0.5)/2)

print(min(x, y), max(x, y) )

"""
N.write(str(x))

F.close()
N.close()
"""
