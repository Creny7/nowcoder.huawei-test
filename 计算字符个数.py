A = input()
B = input()
T = "1234567890"
if B in T:
    print(A.count(B))
else:
    a = B.upper()
    b = B.lower()
    print(A.count(a)+A.count(b))
