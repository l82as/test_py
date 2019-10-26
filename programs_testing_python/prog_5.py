r, g, b = map(int, input().split())
if abs(r - g) > 25 or abs(g - b) > 25 or abs(r - b) > 25:
    print("FORBIDDEN")
else:
    print("ALLOWED")