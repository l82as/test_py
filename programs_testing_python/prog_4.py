s = int(input())
n = int(input())
mass_klad = 0
mass_bagaje = 0
for i in range(n):
    ve = int(input())
    if ve + mass_klad <= s:
        mass_klad += ve
    else:
        mass_bagaje += ve
print(mass_klad)
print(mass_bagaje)