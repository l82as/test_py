a=int(input())
c=int(input())
f=int(input())
if abs(a-c)<=25 and abs(a-f)<=25 and (c-f)<=25:
    print("ALLOWED")
else:
    print("FORBIDDEN")
