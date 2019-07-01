a = input()
A = ""
i = len(a)-1
while i>=0:
    if a[i] in A:
        pass
    else:
        A = A+a[i]
    i = i-1
print(A)
