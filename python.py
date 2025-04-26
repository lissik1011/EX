print("Hello world")
for i in range (10):
    print("a"*i)

a = [2, 2]
j = 1
for i in range (10):
    j += 1
    b = 2*a[j-1] + a[j-2]
    a.append(b)
print(a)

c = [2, 2]
c1 = 1-2**(1/2)
c2 = 1+2**(1/2)
for i in range (2, 12):
    f = c1**i + c2**i
    c.append(f)
print(c)
