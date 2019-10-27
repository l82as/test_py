x,y,z=map(int, input().split())

if abs(x-y)<=25 and abs(x-z)<=25 and (y-z)<=25:
    print("ALLOWED")
else:
    print("FORBIDDEN")
