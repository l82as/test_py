a = int(input())
b = int(input())

if (b//a)%2 == 0:
    print(b%a)
else:
    print(a - b%a)
