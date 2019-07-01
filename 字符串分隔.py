A = []
while True:
    try:
        A.append(input())
    except:
        break
i = 0
while i<len(A):
    while True:
        if len(A[i])>8:
            print(A[i][0:8])
            A[i] = A[i][8:len(A[i])]
        else:
            print(A[i]+((8-len(A[i]))*"0"))
            break
    i = i+1
