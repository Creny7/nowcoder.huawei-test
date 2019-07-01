a = input()
i = 0
while i<len(a):
    if a[i] in a[i+1:len(a)]:
        a = a[0:i]+a[i+1:len(a)]
        i = i-1
    i = i+1
i = 0
b = 0
while i<len(a):
    if 0<=ord(a[i]) and ord(a[i])<=127:
        b = b+1   
    i = i+1
print(b)
