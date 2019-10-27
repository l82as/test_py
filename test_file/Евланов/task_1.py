a = int(input())
b = int(input())


if (b//a)%2==0:
    x=b%a
elif (b//a)%2!=0:
    x=a-b%a
print(x)

