x=int(input())
y=int(input())
z=int(input())
if abs(x-y)<=25 and abs(x-z)<=25 and (y-z)<=25:
    print("ALLOWED")
else:
    print("FORBIDDEN")
