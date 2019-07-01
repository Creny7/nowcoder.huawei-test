a = int(input())
i = 0
A = []
while i<a:
    A.append(input())
    i = i+1
A = sorted(A)
i = 0
while i<a:
    print(A[i])
    i = i+1
