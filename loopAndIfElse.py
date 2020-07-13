# while
a, b = 0, 1
list = []
while b < 10:
    print(b, sep=',', end=',')
    a, b = b, a+b
    list.append(b)

print(b, sep=",")
