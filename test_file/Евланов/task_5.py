a,b,c = map(int,input().split()) 
if abs(a-b)<=25 and abs(a-c)<=25:
    print("ALLOWED")
else:
    print("FORBIDDEN")

