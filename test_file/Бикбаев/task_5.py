r,g,b=map(int,input().split())
if abs(r-g)<=25 and abs(g-b)<=25 and abs(r-b)<=25:
    print("ALLOWED")
else:
    print("FORBIDDEN")
