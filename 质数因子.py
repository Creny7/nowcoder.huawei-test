a = int(input())
def panduan(a):
    i = 2
    flag = 0
    while i<a-1:
        if a%i==0:
            flag = 1
            break
        i = i+1
    if flag == 1:
        return 0
    else:
        return 1
A = ""
i = 2
j = 2

while i<=a:
    if a%i==0:
        if panduan(i)==1:
            A = A+str(i)+" "
            a = a/i
            i = 1
    i = i+1
    
print(A)  
