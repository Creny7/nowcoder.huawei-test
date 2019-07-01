a = int(input())
i = 0
A = []
B = []
while i<a:
    b = input().split(" ")
    A.append(int(b[0]))
    B.append(int(b[1]))
    i = i+1
i = 0
j = 1
while i<len(A):
    while j<len(A):
        if A[i] == A[j]:
            B[i] = B[i]+B[j]
            del B[j]
            del A[j]
            j = j-1
        j = j+1
    i = i+1
    j = i+1
    

i = 0
j = 1
while i<len(A):
    while j<len(A):
        if A[i]>A[j]:
            c = A[i]
            A[i] = A[j]
            A[j] = c
            c = B[i]
            B[i] = B[j]
            B[j] = c
            
        j = j+1
    i = i+1
    j = i+1
    
    
i = 0
while i<len(A):
    print(str(A[i])+" "+str(B[i]))
    i = i+1
