a, b, c = map(int, input("a, b, c = ").split())

if abs(a-b)<=25 and abs(a-c)<=25 and abs(b-c)<=25:
    print("Allowed")
elif abs(a-b)>25 or abs(a-c)>25 or abs(b-c)>25:
    print("Forbidden")
