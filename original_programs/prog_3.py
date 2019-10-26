def ost_ned(a, b):
    s = a[:b] + a[b+1:]
    s_d = 0
    for i in s:
        s_d += int(i)
    new_dig = 9 - s_d % 3
    return a[:b] + str(new_dig) + a[b+1:]
a = input()
max_1 = int(a)

for i in range(len(a)):
     k = ost_ned(a, i)
     if int(k) > max_1:
         max_1 = int(k)

if max_1 == int(a):
    max_1 = int(a)-3
print(max_1)